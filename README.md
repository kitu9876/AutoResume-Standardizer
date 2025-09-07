poetry init
poetry add llama-index-llms-google-genai llama-index

poetry add email-validator
poetry run python services/resume_extraction_service/app/main.py

# AutoResume-Standardizer
The Gen-AI Resume Standardizer is a generative AI–powered application designed to automatically extract, structure, and standardize resume data from unstructured documents (PDF/DOCX).
