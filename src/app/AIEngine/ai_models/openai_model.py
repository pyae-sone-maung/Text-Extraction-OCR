from openai import OpenAI

from src.app.AIEngine.prompt import RESUME_EXTRACTION_PROMPT
from .abstract_ai_model import AbstractTextModel, AbstractImageModel

class OpenAIModel(AbstractTextModel, AbstractImageModel):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.PROMPT_TEMPLATE = RESUME_EXTRACTION_PROMPT

    def generate_text(self, prompt: str, **kwargs):
        formatted_prompt = self.PROMPT_TEMPLATE.format(resume_text=prompt)

        client = OpenAI(api_key=self.api_key)
        response = client.responses.create(
            model="gpt-4o-mini",
            input=formatted_prompt
        )
        print(response)

    def generate_image(self, prompt: str, **kwargs):
        pass