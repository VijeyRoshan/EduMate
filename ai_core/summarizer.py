from .ollama_handler import query_ollama

# Loads the summarization prompt template and queries the LLM

def summarize_text(text: str) -> str:
    """
    Summarize the given text using the LLM via Ollama.
    """
    try:
        with open('EduMate/ollama_prompts/summarize.txt', 'r', encoding='utf-8') as f:
            prompt_template = f.read()
    except Exception:
        prompt_template = "Summarize the following text: {text}"
    prompt = prompt_template.replace('{text}', text)
    return query_ollama(prompt)
