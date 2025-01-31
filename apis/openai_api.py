from apis.base_generation_api import BaseGenerationAPIClient
from openai import OpenAI


class OpenAIClient(BaseGenerationAPIClient):
    def __init__(self, api_key, model):
        super().__init__(api_key, model)

    def generate(self, prompt) -> str:
        client = OpenAI(api_key=self.api_key)

        completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "developer", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content
