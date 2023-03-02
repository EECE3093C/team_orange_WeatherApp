import json
import requests

latitude = str(39.10)
longitude = str(84.51)
temp_unit = "fahrenheit"
windspeed_unit = "mph"
precipitation_unit = "inch"
timezone = "America%2FNew_York"
weather_api_url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&daily=weathercode&current_weather=true&temperature_unit=" + temp_unit +"&windspeed_unit=" + windspeed_unit + "&precipitation_unit=" + precipitation_unit +"&timezone=" + timezone

response = requests.get(weather_api_url).json()
with open('./WMO_Codes.json', 'r',encoding= 'UTF-8') as file:
    wmo_codes = json.loads(file.read())

print ("The weather is " + wmo_codes[str(response['current_weather']['weathercode'])])