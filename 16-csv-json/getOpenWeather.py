#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = 'YOU_DON"T_GET_IT_HERE'

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&appid=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather description.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('In 3 hours:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('In 6 hours:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
