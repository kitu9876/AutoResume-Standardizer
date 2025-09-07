from llama_index.llms.google_genai import GoogleGenAI
from dotenv import load_dotenv
import os
import json
import re
from ..models.resume_info import ResumeInfo

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure directly without GoogleGenAIConfig
llm = GoogleGenAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    response_mime_type="application/json",  # enforce JSON
    temperature=0,  # deterministic outputs
)

