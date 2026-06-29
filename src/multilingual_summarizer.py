from langdetect import detect
from deep_translator import GoogleTranslator

from src.abstractive_summarizer import abstractive_summary


def multilingual_summary(text):
    try:
        lang = detect(text)
    except:
        lang = "en"

    # If English → direct summary
    if lang == "en":
        return abstractive_summary(text)

    # 🔁 Translate to English
    translated_text = GoogleTranslator(source='auto', target='en').translate(text)

    # 🧠 Summarize
    summary_en = abstractive_summary(translated_text)

    # 🔁 Translate back to original language
    final_summary = GoogleTranslator(source='en', target=lang).translate(summary_en)

    return final_summary