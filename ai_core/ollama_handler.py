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

def stream_ollama(prompt: str):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": True
    }
    with requests.post(OLLAMA_API_URL, json=payload, stream=True) as response:
        response.raise_for_status()
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode('utf-8'))
                    # Only yield the 'response' field (the actual text chunk)
                    if 'response' in data:
                        yield data['response']
                except Exception:
                    continue
