from abc import ABC, abstractmethod


class BaseCrawler(ABC):
    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def get_image(self, prompt, save_dir):
        pass
