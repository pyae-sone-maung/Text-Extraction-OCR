from .ai_engine import AIEngine

def run_ai_text_extract(prompt: str, model_name: str):
    ai_engine = AIEngine()
    response = None

    try:
        response = ai_engine.generate_text(prompt, model_name=model_name)
    except Exception as ex:
        print(f"Error running ai task: {ex}")
    return response