// Language code to language name mapping
export const LANGUAGE_MAPPING: Record<string, string> = {
  'en': 'English',
  'ha': 'Hausa',
  'yo': 'Yorùbá (Yoruba)',
  'ig': 'Igbo',
  'pcm': 'Nigerian Pidgin',
  // Add more Nigerian languages as needed
};

/**
 * Decode a language code to its proper language name
 * @param code - The language code (e.g., 'en', 'ha', 'yo')
 * @returns The decoded language name or the original code if not found
 */
export function decodeLanguage(code: string): string {
  return LANGUAGE_MAPPING[code.toLowerCase()] || code;
}

/**
 * Decode an array of language codes to their proper language names
 * @param codes - Array of language codes
 * @returns Array of decoded language names
 */
export function decodeLanguages(codes: string[]): string[] {
  return codes.map(code => decodeLanguage(code));
}

/**
 * Check if a language code is valid (exists in our mapping)
 * @param code - The language code to check
 * @returns True if the code exists in our mapping
 */
export function isValidLanguageCode(code: string): boolean {
  return code.toLowerCase() in LANGUAGE_MAPPING;
} 