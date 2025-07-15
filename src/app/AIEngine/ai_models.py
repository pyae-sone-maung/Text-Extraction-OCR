from abc import ABC, abstractmethod
import google.generativeai as genai
from google.generativeai import types
from src.app.AIEngine.prompt import RESUME_EXTRACTION_PROMPT

class AbstractAIModel(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        pass

class GeminiModel(AbstractAIModel):
    def __init__(self, api_key: str):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self.PROMPT_TEMPLATE = RESUME_EXTRACTION_PROMPT

    generateText = ""


    def generate_text(self, prompt: str, **kwargs) -> str | None:
        formatted_prompt = self.PROMPT_TEMPLATE.format(resume_text=prompt)
        generation_config = types.GenerationConfig(
            temperature=kwargs.get('temperature', 0.1),
        )
        response = self.model.generate_content(
            contents=[formatted_prompt],
            generation_config=generation_config
        )

        if response.candidates:
            first_candidate = response.candidates[0]
            if first_candidate.content and first_candidate.content.parts:
                self.generateText = first_candidate.content.parts[0].text
        return self.generateText

class ChatGPTModel(AbstractAIModel):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_text(self, prompt: str, **kwargs) -> str:
        return f"ChatGPT text generate response."

