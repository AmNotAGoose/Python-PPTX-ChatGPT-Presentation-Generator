import os
import string
from random import choice
from urllib.parse import urlparse
from icrawler.builtin import ImageDownloader, BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
from crawlers import base_crawler


class ICrawlerDownloader(ImageDownloader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.final_image_name = ""
        self.unique_image_name = ""

    def get_filename(self, task, default_ext):
        # url_path = urlparse(task['file_url'])[2]
        # if '.' in url_path:
        #     extension = url_path.split('.')[-1]
        #     if extension.lower() not in [
        #         'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
        #     ]:
        #         extension = default_ext
        # else:
        #     extension = default_ext

        self.final_image_name = "image_" + self.unique_image_name + "." + default_ext

        return self.final_image_name

    def generate_new_name(self):
        self.unique_image_name = ''.join(choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _
                                         in range(16))

    def get_image_name(self):
        return self.final_image_name


class ICrawlerCrawler(base_crawler.BaseCrawler):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def get_image(self, query, save_dir):
        if self.browser == "google":
            crawler = GoogleImageCrawler(downloader_cls=ICrawlerDownloader, storage={'root_dir': save_dir if save_dir
            else os.getcwd()})
        elif self.browser == "bing":
            crawler = BingImageCrawler(downloader_cls=ICrawlerDownloader, storage={'root_dir': save_dir if save_dir
            else os.getcwd()})
        elif self.browser == "baidu":
            crawler = BaiduImageCrawler(downloader_cls=ICrawlerDownloader, storage={'root_dir': save_dir if save_dir
            else os.getcwd()})

        downloader = crawler.downloader

        downloader.generate_new_name()
        crawler.crawl(keyword=query, max_num=1)

        final_image_name = downloader.get_image_name()

        return final_image_name
