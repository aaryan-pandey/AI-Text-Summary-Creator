import warnings
warnings.filterwarnings("ignore")

from flask import Flask, render_template, request
from src.extractive_summarizer import extractive_summary
from src.abstractive_summarizer import abstractive_summary
from src.multilingual_summarizer import multilingual_summary

import PyPDF2
import docx

app = Flask(__name__)

def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""

    if request.method == "POST":
        method = request.form.get("method")
        text = ""

        # File input
        file = request.files.get("file")

        if file and file.filename != "":
            if file.filename.endswith(".pdf"):
                text = read_pdf(file)
            elif file.filename.endswith(".docx"):
                text = read_docx(file)
        else:
            text = request.form.get("text")

        if text:
            if method == "extractive":
                summary = extractive_summary(text)
            elif method == "abstractive":
                summary = abstractive_summary(text)
            else:
                summary = multilingual_summary(text)
            

    return render_template("index.html", summary=summary)


if __name__ == "__main__":
    print("🚀 Starting Flask app...")
    app.run(debug=True, use_reloader=False)