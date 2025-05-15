import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_BASE = "https://api.groq.com/openai/v1"  # Groq’s OpenAI-compatible endpoint
GROQ_MODEL = "llama3-70b-8192"  # or mixtral-8x7b-32768, gemma-7b-it
