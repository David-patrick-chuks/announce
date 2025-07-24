from .prompt import (
    SIMPLIFIED_PROMPT,
    OVERSIMPLIFIED_PROMPT,
    SUMMARY_PROMPT,
    KEYPOINTS_PROMPT,
)

LANGUAGE_CHOICES = [
    ("en", "English"),
    ("ha", "Hausa"),
    ("yo", "Yoruba"),
    ("ig", "Igbo"),
    ("pcm", "Nigerian Pidgin"),
    # Add more Nigerian languages as needed
]


TEXT_TYPE_CHOICES = [
    {"choice": ("original", "Original"), "prompt": ""},
    {"choice": ("simplified", "Simplified"), "prompt": SIMPLIFIED_PROMPT},
    {"choice": ("oversimplified", "Over Simplified"), "prompt": OVERSIMPLIFIED_PROMPT},
    {"choice": ("summary", "Summary"), "prompt": SUMMARY_PROMPT},
    {"choice": ("keypoints", "Key Points"), "prompt": KEYPOINTS_PROMPT},
]


MINISTRY_MAP_CONSOLIDATED = {
    "Ministry of Agriculture and Rural Development": {
        "audience": ["Farmers", "Business", "Policymakers", "Rural Communities"],
        "category": ["Agriculture", "Economy", "Rural Development"],
    },
    "Ministry of Education": {
        "audience": ["Students", "Teachers", "Researchers", "Policymakers"],
        "category": ["Education", "Technology"],
    },
    "Ministry of Health": {
        "audience": ["Healthcare Workers", "Patients", "Researchers", "Policymakers"],
        "category": ["Health", "Welfare"],
    },
    "Ministry of Finance, Budget and National Planning": {
        "audience": ["Business", "Policymakers", "Researchers", "International"],
        "category": ["Economy", "Administration", "Budgeting"],
    },
    "Ministry of Power": {
        "audience": ["Business", "Policymakers", "Utilities", "Citizens"],
        "category": ["Energy", "Infrastructure"],
    },
    "Ministry of Works and Housing": {
        "audience": ["Business", "Policymakers", "Urban Residents", "Engineers"],
        "category": ["Infrastructure", "Housing"],
    },
    "Ministry of Justice": {
        "audience": ["Legal", "Policymakers", "Media", "Researchers"],
        "category": ["Justice", "Administration"],
    },
    "Ministry of Defence": {
        "audience": ["Policymakers", "Military", "Security Agencies", "Citizens"],
        "category": ["Defence", "Security"],
    },
    "Ministry of Women Affairs": {
        "audience": ["Women", "NGOs", "Policymakers", "Children"],
        "category": ["Welfare", "Health", "Gender Equality"],
    },
    "Ministry of Youth and Sports Development": {
        "audience": ["Youth", "Researchers", "Athletes", "Policymakers"],
        "category": ["Youth", "Sports", "Education"],
    },
    "Ministry of Environment": {
        "audience": ["Business", "NGOs", "Researchers", "Policymakers", "Citizens"],
        "category": ["Environment", "Climate Change"],
    },
    "Ministry of Information and Culture": {
        "audience": ["Media", "Business", "Policymakers", "Researchers"],
        "category": ["Information", "Culture", "Administration"],
    },
    "Ministry of Science and Technology": {
        "audience": ["Researchers", "Business", "Scientists", "Policymakers", "Students"],
        "category": ["Technology", "Education", "Innovation"],
    },
    "Ministry of Petroleum Resources": {
        "audience": ["Business", "Policymakers", "International", "Energy Sector"],
        "category": ["Energy", "Economy", "Petroleum"],
    },
    "Ministry of Labour and Employment": {
        "audience": ["Workers", "Business", "Policymakers", "NGOs"],
        "category": ["Labour", "Welfare", "Economy"],
    },
    "Ministry of Transport": {
        "audience": ["Business", "Policymakers", "Commuters", "Logistics"],
        "category": ["Transport", "Infrastructure"],
    },
    "Ministry of Aviation": {
        "audience": ["Business", "Travelers", "Policymakers", "Airlines"],
        "category": ["Aviation", "Transport"],
    },
    "Ministry of Water Resources": {
        "audience": ["Policymakers", "NGOs", "Communities", "Citizens"],
        "category": ["Water", "Environment", "Infrastructure"],
    },
    "Ministry of Communications and Digital Economy": {
        "audience": ["Business", "Policymakers", "Users", "Tech Sector"],
        "category": ["Technology", "Infrastructure", "Digital Economy"],
    },
    "Ministry of Police Affairs": {
        "audience": ["Policymakers", "Police", "Security Agencies", "Citizens"],
        "category": ["Security", "Administration"],
    },
    "Ministry of Humanitarian Affairs, Disaster Management and Social Development": {
        "audience": ["NGOs", "Policymakers", "Vulnerable Groups", "Citizens"],
        "category": ["Welfare", "Disaster Management", "Social Development"],
    },
    # Add more ministries as needed
}

if __name__ == "__main__":
    # To verify the unique counts:
    all_audiences = set()
    all_categories = set()
    for ministry_data in MINISTRY_MAP_CONSOLIDATED.values():
        for aud in ministry_data["audience"]:
            all_audiences.add(aud)
        for cat in ministry_data["category"]:
            all_categories.add(cat)

    print(f"Unique Audiences ({len(all_audiences)}): {sorted(list(all_audiences))}")
    print(f"Unique Categories ({len(all_categories)}): {sorted(list(all_categories))}")
