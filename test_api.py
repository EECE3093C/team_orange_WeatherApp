import requests, json
latitude = str(39.13)
longitude = str(84.51)
temp_unit = "fahrenheit"
windspeed_unit = "mph"
precipitation_unit = "inch"
timezone = "America%2FNew_York"
weather_api_url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&daily=weathercode&current_weather=true&temperature_unit=" + temp_unit +"&windspeed_unit=" + windspeed_unit + "&precipitation_unit=" + precipitation_unit +"&timezone=" + timezone
response = requests.get(weather_api_url)
print(json.dumps(response.json(), indent=4, sort_keys=True))