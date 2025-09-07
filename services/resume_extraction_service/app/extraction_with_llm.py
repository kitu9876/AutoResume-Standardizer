from dotenv import load_dotenv
import os
import json
import re
from .models.resume_info import ResumeInfo
from .prompts.extraction_prompt import EXTRACTION_SYSTEM
from .llm.gemeni_client import llm

def clean_json_output(output: str) -> str:
    """Cleans Gemini's output to ensure it's valid JSON."""
    # Strip whitespace
    cleaned = output.strip()

    # Remove Markdown fences if present
    cleaned = re.sub(r"^```(json)?", "", cleaned, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()

    # If output contains text before/after JSON, try extracting first {...} block
    match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
    if match:
        cleaned = match.group(0)

    return cleaned

def extract_resume_info(text: str) -> ResumeInfo:
    schema = ResumeInfo.model_json_schema()

    prompt = EXTRACTION_SYSTEM.format(schema=json.dumps(schema, indent=2))

    response = llm.complete(prompt + "\n\nResume text:\n" + text)
    raw_output = response.text

    cleaned_output = clean_json_output(raw_output)

    try:
        data = json.loads(cleaned_output)
    except json.JSONDecodeError as e:
        raise ValueError(f"Gemini did not return valid JSON:\n{raw_output}") from e

    return ResumeInfo(**data)
