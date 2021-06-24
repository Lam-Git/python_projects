import requests
from pprint import pprint

# MUST OBTAIN AN API KEY
API_Key = "f7ac1653b910675dd379b66ae7dc7299"

city = input("Enter a city or place you would like to visit :")
base_url = (
    "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q" + city
)

weather_data = requests.get(base_url).json()

pprint(weather_data)
