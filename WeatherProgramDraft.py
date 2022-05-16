import json
from pip._vendor import requests

api_token = '81ab2c5b7610ea0509218bc424ec2ec5'
api_url_base = 'https://api.openweathermap.org/'

def get_weather_info_zip(user_zip_code):
    zip_url = 'https://api.openweathermap.org/data/2.5/weather?zip={user_zip_code},&appid=81ab2c5b7610ea0509218bc424ec2ec5'
    headers = {'Accept' : '81ab2c5b7610ea0509218bc424ec2ec5'}
    r = requests.get(zip_url,headers = headers)
    if r.status_code == 200:
        return json.loads(r.content.decode)
    else:
        return None

def get_weather_info_city(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid=81ab2c5b7610ea0509218bc424ec2ec5'
    headers = {'Accept' : '81ab2c5b7610ea0509218bc424ec2ec5'}
    r2 = requests.get(city_url, headers = headers)
    if r2.status_code == 200:
        return json.loads(r2.content.decode)
    else:
        return None

msg = "Welcome to your local weather forecast program!"
print(msg)
print("This is a service that will show you your local weather forecast based on zip code or city name.")

user_decision=input("Would you like to use a zip code or a city name to get started? Enter 'zip code' or 'city name' to continue. Press 'q' at any time to quit!")
if user_decision == 'zip code':
    user_zip_code=input("Please enter the zip code for the area you would like to see the forecast for!")
    get_weather_info_zip(user_zip_code)

if user_decision == 'city name':
    user_city = input("Please enter the city name you would like to see the forecast for!")
    get_weather_info_city(user_city)

while True:
    if user_decision == 'q':
        print("Thank you for using our service!")
        break
    if user_zip_code == 'q':
        print("Thank you for using our service!")
        break
    if user_city == 'q':
        print("Thank you for using our service!")
        break
    else:
        pass

