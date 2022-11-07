import requests
from pprint import pprint
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter a city Name : ")
URL = base_url + "(YOUR API KEY)" + city_name + "&appid=" + "(YOUR API ID)" 
weather_data = requests.get(URL).json()
print("\nCurrent Weather Data Of " + city_name +":\n")
pprint(weather_data)
