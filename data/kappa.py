from config import Configuration
from typing import Optional, Dict
import requests


class Kappa:
    def __init__(self, username, url) -> None:
        settings = Configuration('config.ini')

        username = settings.get_variable('API', 'api_se_username')
        if username is not None:
            print(f'Username: {username}')
        else:
            print('Username not found in configuration file.')


        url = settings.get_variable('API', 'api_se_endpoint')
        if url is not None:
            print(f'Endpoint url: {url}')
        else:
            print('Endpoint url not found in configuration file.')

    def get_commands(self) -> Optional[Dict[str,str]]:
        endpoint = f"{self.url}{self.username}/commands"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None


