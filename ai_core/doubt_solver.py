from .ollama_handler import query_ollama

# LLM prompt for doubt resolution

# Loads the doubt clarification prompt template and queries the LLM

def clarify_doubt(question: str, context: str = "") -> str:
    """
    Clarify a student's doubt using the LLM via Ollama.
    """
    try:
        with open('EduMate/ollama_prompts/doubt.txt', 'r', encoding='utf-8') as f:
            prompt_template = f.read()
    except Exception:
        prompt_template = "Answer the following question: {question} Context: {context}"
    prompt = prompt_template.replace('{question}', question).replace('{context}', context)
    return query_ollama(prompt)
