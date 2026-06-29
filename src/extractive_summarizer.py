from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.tokenize import sent_tokenize

def extractive_summary(text, num_sentences=3):
    sentences = sent_tokenize(text)
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    
    scores = np.sum(X.toarray(), axis=1)
    
    ranked_sentences = np.argsort(scores)[::-1]
    
    selected = sorted(ranked_sentences[:num_sentences])
    
    summary = " ".join([sentences[i] for i in selected])
    
    return summary
