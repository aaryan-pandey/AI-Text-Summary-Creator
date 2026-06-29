import nltk
import re
nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9. ]', '', text)
    return text

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)