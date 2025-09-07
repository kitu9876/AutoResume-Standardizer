poetry init
poetry add llama-index-llms-google-genai llama-index

poetry add email-validator
poetry run python services/resume_extraction_service/app/main.py