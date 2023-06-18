from config import Configuration
import scrapy


class SeScraper:
    def __init__():
        settings = Configuration('config.ini')
        user_name = settings.get_variable('API', 'api_se_username')
        base_url = settings.get_variable('API', 'api_se_endpoint')
        start_urls = [f'{base_url}{user_name}/commands']

    def parse(self, response):
        html_content = response.content
        content_string = html_content.decode('utf-8')
        print(str(content_string))

