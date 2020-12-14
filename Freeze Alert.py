#! python3
## Weather Alert App
## Created by: Charles Cromer
## Created: 12/01/2020
## Last Modified: 12/13/2020

import json, requests, sys, ezgmail, os, time

# Initializing constants
APPID = 'INSERT YOUR AP ID FROM OPENWEATHER.ORG'
LAT = 'INSERT YOUR AREAS LATTITUDE'
LON = 'INSERT YOUR AREAS LONGITUDE'
PHONE = 'INSERT YOUR PHONES SMS EMAIL ADDRESS HERE'
CREDPATH = r'INSERT THE FILE PATH TO YOUR CREDENTIAL FILE'

# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=imperial&exclude=minutely,daily,hourly&appid={}'.format(LAT, LON, APPID)

# Changes to the working directory of the program
os.chdir(r'{}'.format(CREDPATH))

# Prompts for google sign in if not already done so
ezgmail.init()

# Creates a comparison alert variable
alert = ''

# Creates a loop that will keep the alert checks going infinitely
while True:

    # Saves website response to variable
    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    weatherData = json.loads(response.text)

    # Sends email to PHONE if there is a weather alert for LON and LAT,
    # If no alerts for the area, will do nothing until next check
    try:

        # Saves Current alert as newAlert in order to compares it to alert to see if any new alerts are out
        newAlert = weatherData['alerts'][0]['description']

        # Compares newAlert and alert to see if there has been any change
        # If the alert stays the same, program skips this loop
        # If there is a new alert, the new alert is sent to the phone numbers.
        if newAlert != alert:
            ezgmail.send(PHONE, 'Weather Alert!', weatherData['alerts'][0]['description'])
            
            # Sets newAlert as alert so that upon next loop can determine if there is a new alert
            alert = newAlert

    # If there is no ['alerts'] key/value, catches the error and reports no alerts
    except KeyError:
        pass

    # Pauses program for 5 minutes
    time.sleep(300)
