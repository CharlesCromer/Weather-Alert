Weather Alert App
Created by: Charles Cromer
Contact: Charles.Cromer@gmail.com
Created: 12/01/2020
Last Edit: 12/20/2020

This project demonstraits the use of lists, loops, decision structures, error handling, OS functions, json manipulation, and api integrations. 

There are a few things that must be accomplished prior to running this application successfully on your local environment. You will need to enable the Gmail API, and obtain an application ID from 
Enabling the Gmail API

Go to the following page, and follow the instructions completely:
•	https://developers.google.com/gmail/api/quickstart/python/
•	click the Enable the Gmail API button on that page, and fill out the form that appears.
•	After you’ve filled out the form, the page will present a link to the credentials.json file, which you’ll need to download and place in the same folder as your .py file. The credentials.json file contains the Client ID and Client Secret information, which you should treat the same as your Gmail password and not share with anyone else.
•	Then, in the interactive shell, enter the following code:

>>> import ezgmail, os
>>> os.chdir(r'C:\path\to\credentials_json_file')
>>> ezgmail.init()

•	Make sure you set your current working directory to the same folder that credentials.json is in and that you’re connected to the internet. The ezgmail.init() function will open your browser to a Google sign-in page. Enter your Gmail address and password. The page may warn you “This app isn’t verified,” but this is fine; click Advanced and then Go to Quickstart (unsafe). (If you write Python scripts for others and don’t want this warning appearing for them, you’ll need to learn about Google’s app verification process, which is beyond the scope of this book.) When the next page prompts you with “Quickstart wants to access your Google Account,” click Allow and then close the browser.
•	A token.json file will be generated to give your Python scripts access to the Gmail account you entered. The browser will only open to the login page if it can’t find an existing token.json file. With credentials.json and token.json, your Python scripts can send and read emails from your Gmail account without requiring you to include your Gmail password in your source code.


Enabling the OpenWeatherMap.Org API

•	Visit https://openweathermap.org/api/ in your browser and sign up for a free account to obtain an API key, also called an app ID, which for the OpenWeatherMap service is a string code that looks something like '30144aba38018987d84710d0e319281e'. You don’t need to pay for this service unless you plan on making more than 60 API calls per minute. Keep the API key secret; anyone who knows it can write scripts that use your account’s usage quota.
