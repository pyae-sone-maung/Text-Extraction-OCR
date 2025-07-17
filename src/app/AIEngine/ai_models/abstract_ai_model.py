from abc import ABC, abstractmethod

class AbstractTextModel(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        pass

class AbstractImageModel(ABC):
    @abstractmethod
    def generate_image(self, prompt: str, **kwargs):
        pass