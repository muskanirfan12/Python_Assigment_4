import requests
from pprint import pprint

API_KEY = 'yahan tumhari api key'

city = input("Enter the city name: ")

base_url = f"https://api.openweathermap.org/data/2.5/weather?q=karachi&appid=9f7162f4122273db416c18be1e362f1d&units=metric"

response = requests.get(base_url)
weather_data = response.json()

pprint(weather_data)

if weather_data['cod'] == '404':
    print("City not found ❌")
else:
    print("City found ✅")
