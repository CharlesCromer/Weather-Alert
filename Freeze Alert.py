#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = '22707584ea58c4a1bb1727bbc6aea7fd'

import json, requests, sys


# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/onecall?lat=30.2455&lon=-85.6483&units=imperial&exclude=minutely,daily,hourly&appid=22707584ea58c4a1bb1727bbc6aea7fd'
response = requests.get(url)
response.raise_for_status()


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)


#print(weatherData['alerts'])
#print()
#print(weatherData['alerts'][0]['event'])
print(weatherData['alerts'][0]['description'])





