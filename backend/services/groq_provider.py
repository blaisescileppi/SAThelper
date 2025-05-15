import requests
from config import GROQ_API_KEY, GROQ_API_BASE, GROQ_MODEL

class GroqProvider:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

    def generate_test(self, prompt: str):
        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content": "You are a SAT tutor."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        response = requests.post(f"{GROQ_API_BASE}/chat/completions", json=payload, headers=self.headers)
        return response.json()["choices"][0]["message"]["content"]

    def chat_reply(self, messages: list):
        payload = {
            "model": GROQ_MODEL,
            "messages": messages,
            "temperature": 0.7
        }
        response = requests.post(f"{GROQ_API_BASE}/chat/completions", json=payload, headers=self.headers)
        return response.json()["choices"][0]["message"]["content"]
