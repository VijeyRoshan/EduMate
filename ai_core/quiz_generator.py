from .ollama_handler import query_ollama, stream_ollama

# LLM prompt for quiz creation

# Loads the quiz generation prompt template and queries the LLM

def generate_quiz(topic: str, num_questions: int = 5) -> str:
    """
    Generate a quiz for the given topic using the LLM via Ollama.
    """
    try:
        with open('EduMate/ollama_prompts/quiz.txt', 'r', encoding='utf-8') as f:
            prompt_template = f.read()
    except Exception:
        prompt_template = "Generate a quiz with {num_questions} questions on the topic: {topic}"
    prompt = prompt_template.replace('{topic}', topic).replace('{num_questions}', str(num_questions))
    return query_ollama(prompt)

def generate_quiz_stream(topic: str, num_questions: int = 5):
    """
    Stream quiz generation for the given topic using the LLM via Ollama.
    """
    try:
        with open('EduMate/ollama_prompts/quiz.txt', 'r', encoding='utf-8') as f:
            prompt_template = f.read()
    except Exception:
        prompt_template = "Generate a quiz with {num_questions} questions on the topic: {topic}"
    prompt = prompt_template.replace('{topic}', topic).replace('{num_questions}', str(num_questions))
    return stream_ollama(prompt)
