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

def read_weather_code(weather_code):
    """Returns string weather condition from weather code"""
    with open('./WMO_Codes.json', 'r',encoding= 'UTF-8') as file:
        wmo_codes = json.loads(file.read())
    return wmo_codes[str(weather_code)]

def pull_weather_code(input_json):
    """Returns weather code from api response .json"""
    return input_json['current_weather']['weathercode']

print ("The weather is " + read_weather_code(pull_weather_code(response)))