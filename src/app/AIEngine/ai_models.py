from abc import ABC, abstractmethod
import google.generativeai as genai
from google.generativeai import types

from openai import OpenAI

from src.app.AIEngine.prompt import RESUME_EXTRACTION_PROMPT

class AbstractAIModel(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        pass

class GeminiModel(AbstractAIModel):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.PROMPT_TEMPLATE = RESUME_EXTRACTION_PROMPT

    def generate_text(self, prompt: str, **kwargs) -> str | None:
        response_text = ""
        formatted_prompt = self.PROMPT_TEMPLATE.format(resume_text=prompt)

        client = genai.GenerativeModel("gemini-2.5-flash")
        genai.configure(api_key=self.api_key)
        generation_config = types.GenerationConfig(
            temperature=kwargs.get('temperature', 0.1),
        )
        response = client.generate_content(
            contents=[formatted_prompt],
            generation_config=generation_config
        )

        if response.candidates:
            first_candidate = response.candidates[0]
            if first_candidate.content and first_candidate.content.parts:
                response_text = first_candidate.content.parts[0].text
        return response_text

class OpenAIModel(AbstractAIModel):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.PROMPT_TEMPLATE = RESUME_EXTRACTION_PROMPT

    def generate_text(self, prompt: str, **kwargs):
        formatted_prompt = self.PROMPT_TEMPLATE.format(resume_text=prompt)

        client = OpenAI(api_key=self.api_key)
        response = client.responses.create(
            model="gpt-4.1",
            input = formatted_prompt
        )
        print(response)

