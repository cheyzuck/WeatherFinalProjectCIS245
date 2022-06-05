import json
from pip._vendor import requests
import datetime

api_token = '5e66b8748eb4cb02edfc37a4a1025503'

## zip code functions##

def display_current_weather_info_zip(user_zip_code):
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r = requests.get(url,headers=headers,params=parameters)
    response_dict=r.json()
    try:
        print("")
        print(f"Here is your current weather for {response_dict['name']}: \n{response_dict['weather'][0]['main']}")
        print(f"Description: {response_dict['weather'][0]['description']}")
        print(f"Temperature: {response_dict['main']['temp']} Degrees Farenheit")
        print(f"Feels Like: {response_dict['main']['feels_like']} Degrees Farenheit")
        print(f"Humidity: {response_dict['main']['humidity']}%")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

def display_weather_info_hourly_zip(user_zip_code):
    url = 'https://api.openweathermap.org/geo/1.0/zip?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r5 = requests.get(url,headers=headers,params=parameters)
    response_dict5=r5.json()
    lat = str(response_dict5['lat'])
    lon = str(response_dict5['lon'])

    hourly_daily_url = 'https://api.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r3 = requests.get(hourly_daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    for _ in range(24):
        print("")
        print(f"Hourly Weather for {response_dict5['name']}: \n{response_dict3['hourly'][_]['weather'][0]['main']}")
        print(f"Description: {response_dict3['hourly'][_]['weather'][0]['description']}.")
        print(f"Temperature: {response_dict3['hourly'][_]['temp']} Degrees Farenheit.")
        print(f"Feels Like: {response_dict3['hourly'][_]['feels_like']} Degrees Farenheit.")
        print(f"Humidity: {response_dict3['hourly'][_]['humidity']}%.")
        print(f"Chance of Rain: {response_dict3['hourly'][_]['pop']}%.")
        print("")
    try: 
        for _ in range(_):
            print(f"Weather Alerts for {response_dict5['name']}:\n{response_dict3['alerts'][_]['event']}.")
            print(f"Sender: {response_dict3['alerts'][_]['sender_name']}")
            print(f"Description: \n {response_dict3['alerts'][_]['description']}\n.")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")
        print("")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

def display_weather_info_daily_zip(user_zip_code):
    url = 'https://api.openweathermap.org/geo/1.0/zip?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r5 = requests.get(url,headers=headers,params=parameters)
    response_dict5=r5.json()
    lat = str(response_dict5['lat'])
    lon = str(response_dict5['lon'])

    daily_url = 'https://pro.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : '5e66b8748eb4cb02edfc37a4a1025503', 'units' : 'imperial'}
    r3 = requests.get(daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    count=7
    x=datetime.datetime.now()
    print(f"Daily Weather for {response_dict5['name']} for the next 7 days starting on "+ str(x.strftime("%x"))+".")
    for _ in range(count):
        print("")
        print(f"Weather for Day "+str(_+1)+f" in {response_dict5['name']}: \n{response_dict3['daily'][_]['weather'][0]['main']}")
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
            print(f"Weather Alerts for {response_dict5['name']}:\n{response_dict3['alerts'][_]['event']}.")
            print(f"Sender: {response_dict3['alerts'][_]['sender_name']}")
            print(f"Description: \n {response_dict3['alerts'][_]['description']}\n.")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")
        print("")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

def display_weather_info_5day_zip(user_zip_code):
    url = 'https://api.openweathermap.org/geo/1.0/zip?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'zip' : ''+user_zip_code+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r5 = requests.get(url,headers=headers,params=parameters)
    response_dict5=r5.json()
    lat = str(response_dict5['lat'])
    lon = str(response_dict5['lon'])

    fiveday_url = 'https://api.openweathermap.org/data/2.5/forecast'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat+'', 'lon' : ''+lon+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r4 = requests.get(fiveday_url, headers=headers, params=parameters)
    response_dict4 = r4.json()
    count=40
    try:
        for _ in range(count):
            print("")
            print(f"Forecast for {response_dict4['city']['name']} at {response_dict4['list'][_]['dt_txt']}: \n{response_dict4['list'][_]['weather'][0]['main']}.")
            print(f"Description:{response_dict4['list'][_]['weather'][0]['description']}.")
            print(f"Temperature: {response_dict4['list'][_]['main']['temp']} Degrees Farenheit.")
            print(f"Feels Like: {response_dict4['list'][_]['main']['feels_like']} Degrees Farenheit.")
            print(f"Humidity: {response_dict4['list'][_]['main']['humidity']}%.")
            print(f"Chance of Rain: {response_dict4['list'][_]['pop']}%.")
            print("")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")
        print("")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

## city functions##

def display_current_weather_info_city(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    try:
        print("")
        print(f"Here is your current weather for {response_dict2['name']}: \n{response_dict2['weather'][0]['main']}")
        print(f"Description: {response_dict2['weather'][0]['description']}")
        print(f"Temperature: {response_dict2['main']['temp']} Degrees Farenheit")
        print(f"Feels Like: {response_dict2['main']['feels_like']} Degrees Farenheit")
        print(f"Humidity: {response_dict2['main']['humidity']}%")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

def display_weather_info_hourly_city(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    lat2 = str(response_dict2['coord']['lat'])
    lon2 = str(response_dict2['coord']['lon'])

    hourly_daily_url = 'https://api.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat2+'', 'lon' : ''+lon2+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r3 = requests.get(hourly_daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    for _ in range(24):
        print("")
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
            print("")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")
        print("")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

def display_weather_info_daily_city(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    lat2 = str(response_dict2['coord']['lat'])
    lon2 = str(response_dict2['coord']['lon'])

    hourly_daily_url = 'https://api.openweathermap.org/data/2.5/onecall'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat' : ''+lat2+'', 'lon' : ''+lon2+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r3 = requests.get(hourly_daily_url, headers=headers, params=parameters)
    response_dict3 = r3.json()
    count=7
    x=datetime.datetime.now()
    print(f"Daily Weather for {response_dict2['name']} for the next 7 days starting on "+ str(x.strftime("%x"))+".")
    for _ in range(count):
        print("")
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
            print("")
    except IndexError:
        print("")
    except KeyError:
        print("No weather alerts at this time.")
        print("")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

def display_weather_info_5day_city(user_city):
    city_url = 'https://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'q' : ''+user_city+'', 'APPID': ''+api_token+'', 'units' : 'imperial'}
    r2 = requests.get(city_url, headers=headers,params=parameters)
    response_dict2=r2.json()
    lat2 = str(response_dict2['coord']['lat'])
    lon2 = str(response_dict2['coord']['lon'])

    fiveday_url = 'https://api.openweathermap.org/data/2.5/forecast?'
    headers = {'cache-control' : 'no-cache'}
    parameters = {'lat': ''+lat2+'', 'lon' : ''+lon2+'', 'APPID' : ''+api_token+'', 'units' : 'imperial'}
    r4 = requests.get(fiveday_url, headers=headers, params=parameters)
    response_dict4 = r4.json()
    count=40
    try:
        for _ in range(count):
            print("")
            print(f"Forecast for {response_dict4['city']['name']} at {response_dict4['list'][_]['dt_txt']}: \n{response_dict4['list'][_]['weather'][0]['main']}.")
            print(f"Description:{response_dict4['list'][_]['weather'][0]['description']}.")
            print(f"Temperature: {response_dict4['list'][_]['main']['temp']} Degrees Farenheit.")
            print(f"Feels Like: {response_dict4['list'][_]['main']['feels_like']} Degrees Farenheit.")
            print(f"Humidity: {response_dict4['list'][_]['main']['humidity']}%.")
            print(f"Chance of Rain: {response_dict4['list'][_]['pop']}%.")
            print("")
    except IndexError:
        print("")
    except ConnectionError:
        print("There seems to be an issue with your internet connection. Please check it and try again.")
        print("")

##program, current weather##

msg = "Welcome to your local weather forecast program!"
print(msg)
print("This is a service that will show you your local weather forecast based on zip code or city name. ")

def main():

    user_decision=input("Would you like to use a zip code or a city name to get started? \nZip Codes will be more accurate based on coordinates. Thus, you may see the name of the location vary. \nCity Names will give you the same area, but may not be as specific.\nEnter 'zip code' or 'city name' to continue. Press 'q' at any time to quit! ")

    while True:
        if user_decision == 'zip code':
            break
        if user_decision == 'city name':
            break
        if user_decision == 'q':
            quit()
        if user_decision != 'zip code' or 'city name':
            print("Invalid input! Please try again!")
            user_decision=input()


    if user_decision == 'zip code':
        user_zip_code=input("Please enter the zip code for the area you would like to see the forecast for! ")
        while True:
            try:
                display_current_weather_info_zip(user_zip_code)
            except KeyError: ##someone accidentally enters anything else instead of a zip code.##
                print("Uh oh! Something doesn't look right. Please try again.")
                user_zip_code=input()
            else:
                break      
        if user_zip_code == 'q':
            quit()

    if user_decision == 'city name':
        user_city = input("Please enter the city name you would like to see the forecast for! ")
        while True:
            try:
                display_current_weather_info_city(user_city)
            except KeyError:
                print("Uh oh! Something doesn't look right. Please try again.")
                user_city=input()
            else:
                break
        if user_city == 'q':
            quit()

    ##extended forecast##

    print("Now that you've seen your current weather, would you like to see an extended forecast? \nYou may select from 'hourly', 'daily', or '5 day'. \nPress 'q' to quit.")
    extended_forecast=input()

    while True:
        if extended_forecast == 'hourly':
            break
        if extended_forecast == 'daily':
            break
        if extended_forecast == '5 day':
            break
        if extended_forecast == 'q':
            quit()
        if extended_forecast != 'hourly' or 'daily' or '5 day' or 'q':
            print("Invalid input. Please try again!")
            extended_forecast = input("Enter 'hourly' or 'daily' or '5 day' to continue. ")

    if extended_forecast == 'hourly':
        if user_decision == 'zip code':
            display_weather_info_hourly_zip(user_zip_code)
    if extended_forecast == 'daily':
        if user_decision == 'zip code':
            display_weather_info_daily_zip(user_zip_code)
    if extended_forecast == '5 day':
        if user_decision == 'zip code':
            display_weather_info_5day_zip(user_zip_code)

    if extended_forecast == 'hourly':
        if user_decision == 'city name':
            display_weather_info_hourly_city(user_city)
    if extended_forecast == 'daily':
        if user_decision == 'city name':
            display_weather_info_daily_city(user_city)
    if extended_forecast == '5 day':
        if user_decision == 'city name':
            display_weather_info_5day_city(user_city)

    ##extended forecast 2##

    print("Would you like to see an extended forecast again? \nYou may select from 'hourly' 'daily' or '5 day'. \n Press 'q' to quit.")
    decision2=input()

    while True:
        if decision2 == 'hourly':
            break
        if decision2 == 'daily':
            break
        if decision2 == '5 day':
            break
        if decision2 == 'q':
            quit()
        if decision2 != 'hourly' or 'daily' or '5 day' or 'q':
            print("Invalid input. Please try again!")
            decision2 = input("Enter 'hourly' or 'daily' or '5 day' to continue. ")

    if decision2 == 'hourly':
        if user_decision == 'zip code':
            display_weather_info_hourly_zip(user_zip_code)
    if decision2 == 'daily':
        if user_decision == 'zip code':
            display_weather_info_daily_zip(user_zip_code)
    if decision2 == '5 day':
        if user_decision == 'zip code':
            display_weather_info_5day_zip(user_zip_code)

    if decision2 == 'hourly':
        if user_decision == 'city name':
            display_weather_info_hourly_city(user_city)
    if decision2 == 'daily':
        if user_decision == 'city name':
            display_weather_info_daily_city(user_city)
    if decision2 == '5 day':
        if user_decision == 'city name':
            display_weather_info_5day_city(user_city)

    ##final extended forecast##

    print("Would you like to see an extended forecast a final time?")
    print("You may select from 'hourly' 'daily' or '5 day'. ")
    decision3=input()

    while True:
        if decision3 == 'hourly':
            break
        if decision3 == 'daily':
            break
        if decision3 == '5 day':
            break
        if decision3 == 'q':
            quit()
        if decision3 != 'daily' or '5 day' or 'q':
            print("Invalid input. Please try again!")
            decision3 = input("Enter 'hourly' or 'daily' or '5 day' to continue. ")

    if decision3 == 'hourly':
        if user_decision == 'zip code':
            display_weather_info_hourly_zip(user_zip_code)
    if decision3 == 'daily':
        if user_decision == 'zip code':
            display_weather_info_daily_zip(user_zip_code)
    if decision3 == '5 day':
        if user_decision == 'zip code':
            display_weather_info_5day_zip(user_zip_code)

    if decision3 == 'hourly':
        if user_decision == 'city name':
            display_weather_info_hourly_city(user_city)
    if decision3 == 'daily':
        if user_decision == 'city name':
            display_weather_info_daily_city(user_city)
    if decision3 == '5 day':
        if user_decision == 'city name':
            display_weather_info_5day_city(user_city)

    ##after 3 views##

main()

print("You've viewed 3 different extended forecasts for your area! \nWould you like to look up another? Click 'y' for yes, or anything else for no!")
again=input()

while True:
    if again == 'y':
        main()
    else:
        print("Thank you for using this service! Goodbye!")
        break