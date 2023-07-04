"""Module that translates from English to French and the other way around"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """Translates english_text to French, returns the French text"""
    translator = MyMemoryTranslator(source="english", target="french")
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    """Translates french_text to English, returns the English text"""
    translator = MyMemoryTranslator(source="french", target="english")
    english_text = translator.translate(french_text)
    return english_text
