import os
# from services.resume_extraction_service.app.load_document import (
#     extract_text_from_pdf,
#     extract_text_from_docx,
# )

# from app.extraction_with_llm import extract_resume_info
# from template_renderer import render_resume_docx

from .extraction_with_llm import extract_resume_info
from .load_document import extract_text_from_pdf, extract_text_from_docx
from .template_renderer import render_resume_docx

RESUME_INPUT_DIR = "Assignment1-GenAI"         # folder where input resumes are stored
RESUME_OUTPUT_DIR = "standardized"  

def process_resume(file_path: str, output_dir: str = RESUME_OUTPUT_DIR):
    # 1. Extract text
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_docx(file_path)

    # 2. LLM → structured info
    resume_info = extract_resume_info(text)

    # 3. Output filename
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = os.path.join(output_dir, f"{base_name}_standardized.docx")

    # 4. Generate standardized docx
    os.makedirs(output_dir, exist_ok=True)
    render_resume_docx(resume_info, output_file)

    print(f"✅ Resume generated: {output_file}")
    return output_file


if __name__ == "__main__":
    # Process all resumes in the input folder
    for file_name in os.listdir(RESUME_INPUT_DIR):
        if file_name.lower().endswith((".pdf", ".docx")):
            file_path = os.path.join(RESUME_INPUT_DIR, file_name)
            process_resume(file_path)
