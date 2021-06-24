import requests
from pprint import pprint

# MUST OBTAIN AN API KEY
API_Key = "1b8ffa6ce5fc8154f0cb373b301b9a52"

city = input("Enter a city:")
base_url = (
    "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q" + city
)

weather_data = request.get(base_url).json()

pprint(weather_data)
