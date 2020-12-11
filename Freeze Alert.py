#! python3

import json, requests, sys, ezgmail, os, time

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

# Prompts for google sign in if not already done so
ezgmail.init()

# Creates a loop that will keep the alert checks going infinitely
while True:

    # Sends email to PHONE if there is a weather alert for LON and LAT,
    # If no alerts for the area, will do nothing until next check
    try:
        ezgmail.send(PHONE, 'Weather Alert!', weatherData['alerts'][0]['description'])
    except KeyError:  # If there is no ['alerts'] key/value, catches the error and reports no alerts
        pass

    # Pauses program for 5 minutes
    time.sleep(300)
