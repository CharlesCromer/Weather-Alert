#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = '<your api key from openweather.org with no <> brackets>'
LAT = ''
LON = ''

import json, requests, sys


# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=imperial&exclude=minutely,daily,hourly&appid={}'.format(LAT, LON, APPID)
response = requests.get(url)
response.raise_for_status()


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Prints the description of any weather alerts, will later be replaced with sending email-to-text code.
try:
    print(weatherData['alerts'][0]['description'])
except KeyError:  # If there is no ['alerts'] key/value, catches the error and reports no alerts
    print('No Alerts :)')



