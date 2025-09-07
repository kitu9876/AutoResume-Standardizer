poetry init
poetry add llama-index-llms-google-genai llama-index

poetry add email-validator
poetry run python services/resume_extraction_service/app/main.py

# AutoResume-Standardizer

The GenAI Resume Standardizer is a generative AI–powered application designed to automatically extract, structure, and standardize resume data from unstructured documents (PDF/DOCX). Using advanced language models, the system parses resumes to identify key details such as personal information, skills, education, experiences, certifications, and languages.

Once extracted, the information is transformed into a consistent structured format and exported into a clean, standardized resume document (DOCX). This ensures uniformity across resumes, making it easier for recruiters, hiring managers, and automated HR systems to review candidate profiles efficiently.

## Key Features

📄 Multi-format Input – Supports both PDF and DOCX resumes.

🤖 Generative AI Parsing – Extracts structured data using schema-driven JSON outputs.

🎯 Standardized Output – Generates professional, consistent resume formats automatically.

⚡ Automation Ready – Reduces manual formatting effort and improves recruiter efficiency.

## Potential Extensions

1. Integration with ATS (Applicant Tracking Systems).

2. Support for multilingual resumes.

3. Scoring/ranking candidates based on extracted features.
