from bs4 import BeautifulSoup
from config import Configuration
import requests

settings = Configuration('config.ini')
user_name = settings.get_variable('API', 'api_se_username')
base_url = settings.get_variable('API', 'api_se_endpoint')

file_path = f"{user_name}_page.html"
commands_url = f"{base_url}/commands"

response = requests.get(commands_url)

soup = BeautifulSoup(response.content, 'html.parser')

file = open(file_path, 'x')
file.write(str(soup))
file.close()

print(soup)

cards = soup.find_all('m-card')
for card in cards:
    print(card.get('class'))

print('end of program')

