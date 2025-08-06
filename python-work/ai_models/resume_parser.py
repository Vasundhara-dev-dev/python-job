# ai_models/resume_parser.py
import os
from PyPDF2 import PdfReader
import docx

def parse_resume(file_path: str) -> str:
    """
    Extract text from a PDF or DOCX resume.
    Returns extracted text as a string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    text = ""

    # Handle PDF files
    if file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + " "

    # Handle DOCX files
    elif file_path.lower().endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + " "

    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")

    return text.strip()



