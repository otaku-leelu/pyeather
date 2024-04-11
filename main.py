import datetime as dt
from datetime import timezone
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "your_api_key_here"

CITY = input("Enter the city: ").capitalize()


def kToCF(kelvin):
    celsius = kelvin - 273.15
    return celsius


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius = kToCF(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kToCF(feels_like_kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(
    response['sys']['sunrise'] + response['timezone'], tz=timezone.utc)
sunset_time = dt.datetime.fromtimestamp(
    response['sys']['sunset'] + response['timezone'], tz=timezone.utc)

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time.time()}")
print(f"Sun sets in {CITY} at {sunset_time.time()}")
