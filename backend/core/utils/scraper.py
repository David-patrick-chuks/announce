import re
import requests
from bs4 import BeautifulSoup
from .http_client import get_retry_session
from .secrets import get_pib_secrets, get_payload
from ..constants.response_models import (
    PressReleaseMetadata,
    PressReleaseMetadataList,
    PressReleaseContent,
)
from datetime import datetime
from django.utils import timezone
import pytz
import logging

logger = logging.getLogger(__name__)

session = get_retry_session()


def get_press_release_metadata():
    # Nigerian news scraping: Premium Times headline stories
    url = "https://www.premiumtimesng.com/category/news/headlines"
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        logger.error(f"Error fetching Nigerian news: {e}")
        return PressReleaseMetadataList()

    soup = BeautifulSoup(response.text, "html.parser")
    press_releases_metadata = []

    # Each story is in an article tag with class 'post'
    articles = soup.find_all("article", class_="post")
    for article in articles:
        # Title
        title_tag = article.find("h2", class_="entry-title")
        if not title_tag or not title_tag.a:
            continue
        title = title_tag.get_text(strip=True)
        href = title_tag.a["href"]
        full_url = href if href.startswith("http") else f"https://www.premiumtimesng.com{href}"

        # Date (if available)
        date_tag = article.find("time", class_="entry-date")
        date_published = None
        if date_tag and date_tag.has_attr("datetime"):
            try:
                date_published = datetime.fromisoformat(date_tag["datetime"])
                # Localize to Africa/Lagos
                lagos = pytz.timezone("Africa/Lagos")
                date_published = lagos.localize(date_published)
                if str(timezone.get_current_timezone()) != "Africa/Lagos":
                    date_published = date_published.astimezone(timezone.get_current_timezone())
            except Exception:
                date_published = None

        # Ministry is not available; set to 'N/A' or extract from context if possible
        ministry = "N/A"

        press_releases_metadata.append(
            PressReleaseMetadata(ministry=ministry, title=title, url=full_url)
        )
    return PressReleaseMetadataList(press_releases=press_releases_metadata)


def get_press_release_content(url):
    try:
        pr_response = session.get(url, timeout=10)
        pr_response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return PressReleaseContent()

    pr_soup = BeautifulSoup(pr_response.text, "html.parser")
    # Main content is in div with class 'entry-content'
    content = pr_soup.find("div", class_="entry-content")
    date_div = pr_soup.find("time", class_="entry-date")

    date_published = None
    if date_div and date_div.has_attr("datetime"):
        try:
            date_published = datetime.fromisoformat(date_div["datetime"])
            lagos = pytz.timezone("Africa/Lagos")
            date_published = lagos.localize(date_published)
            if str(timezone.get_current_timezone()) != "Africa/Lagos":
                date_published = date_published.astimezone(timezone.get_current_timezone())
            if date_published > timezone.now():
                date_published = timezone.now()
        except Exception:
            date_published = None

    if content:
        return PressReleaseContent(
            content=BeautifulSoup(str(content), "html.parser").prettify(),
            date_published=date_published,
            pib_hq=None,  # Not applicable for Nigeria
        )
    return PressReleaseContent()


def get_today_date():
    # return day month year, as a tuple string
    today = datetime.now()
    return (str(today.day), str(today.month), str(today.year))
