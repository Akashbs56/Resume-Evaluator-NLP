import pdfplumber
from docx import Document
import os


def extract_text(file_path):
    """
    Extract text from PDF or DOCX resume.
    """

    # Get file extension
    extension = os.path.splitext(file_path)[1].lower()

    # PDF
    if extension == ".pdf":
        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    # DOCX
    elif extension == ".docx":

        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    else:
        return "Unsupported File Format"