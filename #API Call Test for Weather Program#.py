#API Call Test for Weather Program#

import json
from pip._vendor import requests

api_token = '81ab2c5b7610ea0509218bc424ec2ec5'
api_url_base = 'https://api.openweathermap.org/'

url = 'https://api.openweathermap.org/data/2.5/weather?zip=17551,&appid=81ab2c5b7610ea0509218bc424ec2ec5'
headers = {'Accept' : '81ab2c5b7610ea0509218bc424ec2ec5'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
print(response_dict.keys())
print(f"Current Weather: {response_dict['weather']}")