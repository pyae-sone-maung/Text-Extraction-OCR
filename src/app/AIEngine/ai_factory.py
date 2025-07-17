import os
from .ai_models.abstract_ai_model import AbstractTextModel
from .ai_models.gemini_model import GeminiModel
from .ai_models.openai_model import  OpenAIModel

class AIModelFactory:
    @staticmethod
    def get_model(model_name: str) -> AbstractTextModel:
        model_name_lower = model_name.lower()
        api_key_env_name = f"{model_name_lower.upper()}_API_KEY"
        api_key = os.getenv(api_key_env_name)

        if not api_key:
            raise ValueError(f"API Key not found for model: {model_name}")

        if model_name_lower == "gemini":
            return GeminiModel(api_key=api_key)
        elif model_name_lower == "openai":
            return OpenAIModel(api_key=api_key)
        else:
            raise ValueError(f"Unsupported model: {model_name}")