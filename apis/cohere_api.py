from apis.base_generation_api import BaseGenerationAPIClient
import cohere


class CohereAPIClient(BaseGenerationAPIClient):
    def __init__(self, api_key, model):
        super().__init__(api_key, model)

    def generate(self, prompt):
        co = cohere.ClientV2(api_key=self.api_key)
        res = co.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return res.message.content[0].text
