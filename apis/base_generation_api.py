from abc import ABC, abstractmethod


class BaseGenerationAPIClient(ABC):
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model

    @abstractmethod
    def generate(self, prompt):
        pass
