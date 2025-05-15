import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_test(subject: str, difficulty: str) -> str:
    prompt = f"Create a {difficulty}-level SAT {subject} practice test with 5 multiple choice questions and correct answers."
    body = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=body)
    return response.json()['choices'][0]['message']['content']

def ask_question(question: str) -> str:
    body = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": f"Explain this SAT question: {question}"}],
        "temperature": 0.7
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=body)
    return response.json()['choices'][0]['message']['content']
