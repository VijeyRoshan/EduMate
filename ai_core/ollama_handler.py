# Interface with Ollama (Mistral)

import requests
import json

# OLLAMA_API_URL should point to your local Ollama instance
OLLAMA_API_URL = 'http://localhost:11434/api/generate'
OLLAMA_MODEL = 'mistral'

def query_ollama(prompt: str) -> str:
    """
    Send a prompt to the local Ollama (Mistral) instance and return the response.
    """
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get('response', '').strip()
    except Exception as e:
        return f"[Error communicating with Ollama: {e}]"
