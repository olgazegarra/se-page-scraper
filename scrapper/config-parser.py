import configparser


config = configparser.ConfigParser()

config.read('config.ini')

api_endpoint_url = config.get('API', 'api_se_endpoint')
api_username = config.get('API', 'api_se_username')