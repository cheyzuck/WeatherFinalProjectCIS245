import json
from pip._vendor import requests

api_token = '81ab2c5b7610ea0509218bc424ec2ec5'
api_url_base = 'https://api.openweathermap.org/'

msg = "Welcome to your local weather forecast program!"
print(msg)
print("This is a service that will show you your local weather forecast.")

user_zip_code = input("Please enter the zip code for the area you would like to see a forecast for. Press 'q' at any time to quit.")
user_city = input("Please enter the city name you would like to see a forecast for. Press 'q' at any time to quit.")

while True:
    if user_zip_code == 'q':
        print("Thank you for using our service!")
        break
    if user_city == 'q':
        print("Thank you for using our service!")
        break
    else:
        pass

def get_weather_info_zip():
    user_zip_code = int(user_zip_code)
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={user_zip_code},&appid={api_token}'
    headers = {'Accept' : ''}
    r = requests.get(url, headers=headers)
    print(r)

get_weather_info_zip(user_zip_code)