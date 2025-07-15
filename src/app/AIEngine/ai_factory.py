import os
from .ai_models import AbstractAIModel, GeminiModel, ChatGPTModel

class AIModelFactory:
    def __init__(self):
        pass
    @staticmethod
    def get_model(model_name: str)-> AbstractAIModel:
        model_name_lower = model_name.lower()
        api_key_env_name = f"{model_name_lower.upper()}_API_KEY"
        api_key = os.getenv(api_key_env_name)

        if not api_key:
            raise ValueError(f"API Key not found in model : {model_name}")

        if model_name_lower == "gemini":
            return  GeminiModel(api_key = api_key)
        elif model_name_lower == "chatgpt":
            return  ChatGPTModel(api_key=api_key)
        else:
            raise ValueError(f"Unsupported models : {model_name}")

