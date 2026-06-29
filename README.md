# 🧠 AI Text Summarizer

An AI-powered web application that generates summaries from long text, PDFs, and DOCX files using NLP and Transformer models.

---

## 🚀 Features

- ✂️ Extractive Summarization (TF-IDF)
- 🤖 Abstractive Summarization (BART Transformer)
- 🌍 Multilingual Support (Hindi + others)
- 📄 PDF & DOCX File Upload
- 🎨 Modern Web UI (Flask + HTML/CSS)

---

## 🧠 Technologies Used

- Python
- Flask
- NLTK
- Scikit-learn
- HuggingFace Transformers
- PyPDF2
- python-docx
- Langdetect
- Deep Translator

---

## ⚙️ How It Works

1. User inputs text or uploads file  
2. System extracts text  
3. Selects summarization method  
4. Generates summary using NLP models  

## ▶️ Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/ai-text-summarizer.git
cd ai-text-summarizer

pip install -r requirements.txt
python -m app.app
