from src.app.AIEngine.ai_factory import AIModelFactory
from src.app.AIEngine.ai_models import AbstractAIModel

class AIEngine:
    def __init__(self):
        self.factory = AIModelFactory()
        self._current_model: AbstractAIModel | None = None
        self._current_model_name: str | None = None
        self._initialized_models = {}

    def set_active_model(self, model_name: str):
        model_name_lower = model_name.lower()
        if self._current_model_name != model_name_lower:
            print(f"Active Model : {model_name}")
            if model_name.lower not in self._initialized_models:
                self._initialized_models[model_name_lower] = self.factory.get_model(model_name)
            self._current_model = self._initialized_models[model_name.lower()]
            self._current_model_name = model_name_lower
        else:
            print(f"Model is already active")

    def _get_active_model(self) -> AbstractAIModel:
        if self._current_model is None:
            raise ValueError(f"No active AI model.")
        return  self._current_model

    def generate_text(self, prompt: str, model_name: str = None, **kwargs):
        if model_name:
            self.set_active_model(model_name)
        model = self._get_active_model()
        return  model.generate_text(prompt, **kwargs)

    @staticmethod
    def get_supported_models() -> list[str]:
        return ["gemini", "chatgpt", "deepseek"]