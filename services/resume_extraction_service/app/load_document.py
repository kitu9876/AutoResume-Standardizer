import pdfplumber
import mammoth

def extract_text_from_pdf(file_path: str) -> str:
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def extract_text_from_docx(file_path: str) -> str:
    with open(file_path, "rb") as f:
        result = mammoth.extract_raw_text(f)
    return result.value
