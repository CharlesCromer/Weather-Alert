#! python3

import json, requests, sys, ezgmail, os

# Initializing constants
APPID = 'INSERT YOUR AP ID FROM OPENWEATHER.ORG'
LAT = 'INSERT YOUR AREAS LATTITUDE'
LON = 'INSERT YOUR AREAS LONGITUDE'

# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=imperial&exclude=minutely,daily,hourly&appid={}'.format(LAT, LON, APPID)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Changes to the working directory of the program
os.chdir(r'C:\Users\charl\OneDrive\Documents\GitHub\Weather Alert App')

ezgmail.init()

# Sends email to PHONE if there is a weather alert for LON and LAT
try:
    ezgmail.send(PHONE, 'Weather Alert!', weatherData['alerts'][0]['description'])
except KeyError:  # If there is no ['alerts'] key/value, catches the error and reports no alerts
    #ezgmail.send(PHONE, 'Weather Alert!', 'This is my program sending you a weather alert: No Alerts :)')
    print('No Alerts :)')
