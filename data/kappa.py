from config import Configuration
from typing import Optional, Dict
import requests


class Kappa:
    def __init__(self) -> None:
        settings = Configuration('config.ini')

        self.username = settings.get_variable('API', 'api_se_username')
        if self.username is not None:
            print(f'Username: {self.username}')
        else:
            print('Username not found in configuration file.')

        self.url = settings.get_variable('API', 'api_se_endpoint')
        if self.url is not None:
            print(f'Endpoint url: {self.url}')
        else:
            print('Endpoint url not found in configuration file.')

    def get_commands(self) -> Optional[Dict[str,str]]:
        user_info = self.get_user_info()
        user_id = user_info["_id"]
        endpoint = f"{self.url}/bot/commands/{user_id}/public"
        print(endpoint)
        response = requests.get(endpoint)
        if response.status_code == 200:
            result = response.json()
            keys_to_show = ["enabled", "command", "reply"]
            short_result = [{key: obj[key] for key in keys_to_show} for obj in result]
            return short_result
        else:
            return None
        
    def get_user_info(self) -> Optional[Dict[str,str]]:
        endpoint = f"{self.url}/channels/{self.username}"
        print(endpoint)
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None


