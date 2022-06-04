import json
from pip._vendor import requests
import datetime

api_token = '757d7f58da3fdd3e972a1d3201ec66db'
api_url_base = 'https://api.openweathermap.org/'

## zip code functions##

def display_current_weather_info_zip(user_zip_code):
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r = requests.get(url,headers=headers,params=parameters)
    response_dict=r.json()
    try:
        print(f"Here is your current weather for {response_dict['name']}: \n{response_dict['weather'][0]['main']}")
        print(f"Description: {response_dict['weather'][0]['description']}")
        print(f"Temperature: {response_dict['main']['temp']} Degrees Farenheit")
        print(f"Feels Like: {response_dict['main']['feels_like']} Degrees Farenheit")
        print(f"Humidity: {response_dict['main']['humidity']}%")
    except ConnectionError:
        print("There seems to be an issue with your connection. Check your connection and try again.")

def display_weather_info_hourly(user_zip_code):
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r = requests.get(url,headers=headers,params=parameters)
    response_dict=r.json()
    lat = str(response_dict['coord']['lat'])
    lon = str(response_dict['coord']['lon'])
    hourly_daily_url = 'https://api.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r3 = requests.get(hourly_daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    for _ in range(24):
        print(f"Hourly Weather for {response_dict['name']}: \n{response_dict3['hourly'][_]['weather'][0]['main']}")
        print(f"Description: {response_dict3['hourly'][_]['weather'][0]['description']}.")
        print(f"Temperature: {response_dict3['hourly'][_]['temp']} Degrees Farenheit.")
        print(f"Feels Like: {response_dict3['hourly'][_]['feels_like']} Degrees Farenheit.")
        print(f"Humidity: {response_dict3['hourly'][_]['humidity']}%.")
        print(f"Chance of Rain: {response_dict3['hourly'][_]['pop']}%.")
        print("")
    try: 
        for _ in range(_):
            print(f"Weather Alerts for {response_dict['name']}:\n{response_dict3['alerts'][_]['event']}.")
            print(f"Sender: {response_dict3['alerts'][_]['sender_name']}")
            print(f"Description: \n {response_dict3['alerts'][_]['description']}\n.")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")

def display_weather_info_daily(user_zip_code):
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r = requests.get(url,headers=headers,params=parameters)
    response_dict=r.json()
    lat = str(response_dict['coord']['lat'])
    lon = str(response_dict['coord']['lon'])
    hourly_daily_url = 'https://api.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r3 = requests.get(hourly_daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    count=7
    x=datetime.datetime.now()
    print(f"Daily Weather for {response_dict['name']} for the next 7 days starting on "+ str(x.strftime("%x"))+".")
    for _ in range(count):
        print(f"Weather for Day "+str(_+1)+f" in {response_dict['name']}: \n{response_dict3['daily'][_]['weather'][0]['main']}")
        print(f"Description: {response_dict3['daily'][_]['weather'][0]['description']}.")
        print(f"Minimum Temperature: {response_dict3['daily'][_]['temp']['min']} Degrees Farenheit.")
        print(f"Maximum Temperature: {response_dict3['daily'][_]['temp']['max']} Degrees Farenheit.")
        print(f"Daily Temperature: \nMorning:{response_dict3['daily'][_]['temp']['morn']} Degrees Farenheit.\nDay: {response_dict3['daily'][_]['temp']['day']} Degrees Farenheit.\nEvening: {response_dict3['daily'][_]['temp']['eve']} Degrees Farenheit.\nNight: {response_dict3['daily'][_]['temp']['night']} Degrees Farenheit.")
        print(f"Daily Feels Like: \nMorning:{response_dict3['daily'][_]['feels_like']['morn']} Degrees Farenheit.\nDay: {response_dict3['daily'][_]['feels_like']['day']} Degrees Farenheit.\nEvening: {response_dict3['daily'][_]['feels_like']['eve']} Degrees Farenheit.\nNight: {response_dict3['daily'][_]['feels_like']['night']} Degrees Farenheit.")
        print(f"Daily Humidity: {response_dict3['daily'][_]['humidity']}%.")
        print(f"Daily Chance of Rain: {response_dict3['daily'][_]['pop']}%.")
        print("")

    try:
        for _ in range(_): 
            print(f"Weather Alerts for {response_dict['name']}:\n{response_dict3['alerts'][_]['event']}.")
            print(f"Sender: {response_dict3['alerts'][_]['sender_name']}")
            print(f"Description: \n {response_dict3['alerts'][_]['description']}\n.")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")

def display_weather_info_5day(user_zip_code):
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r = requests.get(url,headers=headers,params=parameters)
    response_dict=r.json()
    lat = str(response_dict['coord']['lat'])
    lon = str(response_dict['coord']['lon'])
    fiveday_url = 'https://api.openweathermap.org/data/2.5/forecast'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r4 = requests.get(fiveday_url, headers=headers, params=parameters)
    response_dict4 = r4.json()
    count=40
    for _ in range(count):
        print(f"Forecast for {response_dict4['city']['name']} at {response_dict4['list'][_]['dt_txt']}: \n{response_dict4['list'][_]['weather'][0]['main']}.")
        print(f"Description:{response_dict4['list'][_]['weather'][0]['description']}.")
        print(f"Temperature: {response_dict4['list'][_]['main']['temp']} Degrees Farenheit.")
        print(f"Feels Like: {response_dict4['list'][_]['main']['feels_like']} Degrees Farenheit.")
        print(f"Humidity: {response_dict4['list'][_]['main']['humidity']}%.")
        print(f"Chance of Rain: {response_dict4['list'][_]['pop']}%.")
        print("")

##city functions##

def display_current_weather_info_city(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    try:
        print(f"Here is your current weather for {response_dict2['name']}: \n{response_dict2['weather'][0]['main']}")
        print(f"Description: {response_dict2['weather'][0]['description']}")
        print(f"Temperature: {response_dict2['main']['temp']} Degrees Farenheit")
        print(f"Feels Like: {response_dict2['main']['feels_like']} Degrees Farenheit")
        print(f"Humidity: {response_dict2['main']['humidity']}%")
    except ConnectionError:
        print("There seems to be an issue with your connection. Check your connection and try again.")

def display_weather_info_hourly(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    lat = str(response_dict2['coord']['lat'])
    lon = str(response_dict2['coord']['lon'])
    hourly_daily_url = 'https://api.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r3 = requests.get(hourly_daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    for _ in range(24):
        print(f"Hourly Weather for {response_dict2['name']}: \n{response_dict3['hourly'][_]['weather'][0]['main']}")
        print(f"Description: {response_dict3['hourly'][_]['weather'][0]['description']}.")
        print(f"Temperature: {response_dict3['hourly'][_]['temp']} Degrees Farenheit.")
        print(f"Feels Like: {response_dict3['hourly'][_]['feels_like']} Degrees Farenheit.")
        print(f"Humidity: {response_dict3['hourly'][_]['humidity']}%.")
        print(f"Chance of Rain: {response_dict3['hourly'][_]['pop']}%.")
        print("")
    try: 
        for _ in range(_):
            print(f"Weather Alerts for {response_dict2['name']}:\n{response_dict3['alerts'][_]['event']}.")
            print(f"Sender: {response_dict3['alerts'][_]['sender_name']}")
            print(f"Description: \n {response_dict3['alerts'][_]['description']}\n.")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")

def display_weather_info_daily(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    lat = str(response_dict2['coord']['lat'])
    lon = str(response_dict2['coord']['lon'])
    hourly_daily_url = 'https://api.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r3 = requests.get(hourly_daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    count=7
    x=datetime.datetime.now()
    print(f"Daily Weather for {response_dict2['name']} for the next 7 days starting on "+ str(x.strftime("%x"))+".")
    for _ in range(count):
        print(f"Weather for Day "+str(_+1)+f" in {response_dict2['name']}: \n{response_dict3['daily'][_]['weather'][0]['main']}")
        print(f"Description: {response_dict3['daily'][_]['weather'][0]['description']}.")
        print(f"Minimum Temperature: {response_dict3['daily'][_]['temp']['min']} Degrees Farenheit.")
        print(f"Maximum Temperature: {response_dict3['daily'][_]['temp']['max']} Degrees Farenheit.")
        print(f"Daily Temperature: \nMorning: {response_dict3['daily'][_]['temp']['morn']} Degrees Farenheit.\nDay: {response_dict3['daily'][_]['temp']['day']} Degrees Farenheit.\nEvening: {response_dict3['daily'][_]['temp']['eve']} Degrees Farenheit.\nNight: {response_dict3['daily'][_]['temp']['night']} Degrees Farenheit.")
        print(f"Daily Feels Like: \nMorning: {response_dict3['daily'][_]['feels_like']['morn']} Degrees Farenheit.\nDay: {response_dict3['daily'][_]['feels_like']['day']} Degrees Farenheit.\nEvening: {response_dict3['daily'][_]['feels_like']['eve']} Degrees Farenheit.\nNight: {response_dict3['daily'][_]['feels_like']['night']} Degrees Farenheit.")
        print(f"Daily Humidity: {response_dict3['daily'][_]['humidity']}%.")
        print(f"Daily Chance of Rain: {response_dict3['daily'][_]['pop']}%.")
        print("")

    try:
        for _ in range(_): 
            print(f"Weather Alerts for {response_dict2['name']}:\n{response_dict3['alerts'][_]['event']}.")
            print(f"Sender: {response_dict3['alerts'][_]['sender_name']}")
            print(f"Description: \n {response_dict3['alerts'][_]['description']}\n.")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")

def display_weather_info_5day(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    lat = str(response_dict2['coord']['lat'])
    lon = str(response_dict2['coord']['lon'])
    fiveday_url = 'https://api.openweathermap.org/data/2.5/forecast'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r4 = requests.get(fiveday_url, headers=headers, params=parameters)
    response_dict4 = r4.json()
    count=40
    for _ in range(count):
        print(f"Forecast for {response_dict4['city']['name']} at {response_dict4['list'][_]['dt_txt']}: \n{response_dict4['list'][_]['weather'][0]['main']}.")
        print(f"Description:{response_dict4['list'][_]['weather'][0]['description']}.")
        print(f"Temperature: {response_dict4['list'][_]['main']['temp']} Degrees Farenheit.")
        print(f"Feels Like: {response_dict4['list'][_]['main']['feels_like']} Degrees Farenheit.")
        print(f"Humidity: {response_dict4['list'][_]['main']['humidity']}%.")
        print(f"Chance of Rain: {response_dict4['list'][_]['pop']}%.")
        print("")

##program##

msg = "Welcome to your local weather forecast program!"
print(msg)
print("This is a service that will show you your local weather forecast based on zip code or city name. ")

##current weather##

user_decision=input("Would you like to use a zip code or a city name to get started? Enter 'zip code' or 'city name' to continue. Press 'q' at any time to quit! ")
if user_decision == 'zip code':
    user_zip_code=input("Please enter the zip code for the area you would like to see the forecast for! ")
    display_current_weather_info_zip(user_zip_code)

if user_decision == 'city name':
    user_city = input("Please enter the city name you would like to see the forecast for! ")
    display_current_weather_info_city(user_city)
while True:
    if user_decision == 'q':
        print('Thank you for using this service!')
        break

##extended forecast##

print("Now that you've seen your current weather, would you like to see an extended forecast? You may select from 'hourly', 'daily', or '5 day'. ")
extended_forecast=input()

if user_decision == 'zip code':
    if extended_forecast == 'hourly':
        display_weather_info_hourly(user_zip_code)
    if extended_forecast == 'daily':
        display_weather_info_daily(user_zip_code)
    if extended_forecast == '5 day':
        display_weather_info_5day(user_zip_code)
    while True:
        if extended_forecast == 'q':
            print("Thank you for using this service!")
            break

if user_decision == 'city name':
    if extended_forecast == 'hourly':
        display_weather_info_hourly(user_city)
    if extended_forecast == 'daily':
        display_weather_info_daily(user_city)
    if extended_forecast == '5 day':
        display_weather_info_5day(user_city)
    while True:
        if extended_forecast == 'q':
            print("Thank you for using this service!")
            break

##another view of extended forecast##

print("Would you like to see an extended forecast again? You may select from 'hourly', 'daily', or '5 day'. ")
decision2=input()

if user_decision == 'zip code':
    if decision2 == 'hourly':
        display_weather_info_hourly(user_zip_code)
    if decision2 == 'daily':
        display_weather_info_daily(user_zip_code)
    if decision2 == '5 day':
        display_weather_info_5day(user_zip_code)
    while True:
        if decision2 == 'q':
            print("Thank you for using this service!")
            break

if user_decision == 'city name':
    if decision2 == 'hourly':
        display_weather_info_hourly(user_city)
    if decision2 == 'daily':
        display_weather_info_daily(user_city)
    if decision2 == '5 day':
        display_weather_info_5day(user_city)
    while True:
        if decision2 == 'q':
            print("Thank you for using this service!")
            break