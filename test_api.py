import requests
weather_api_url = "https://api.open-meteo.com/v1/forecast?latitude=39.13&longitude=-84.51&daily=weathercode&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York"
response = requests.get(weather_api_url)
print(response.json())