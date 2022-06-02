from urllib import request
import requests

API_KEY= "653c24e6dea8feb9a6b4024fce11f04a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    
    print("Weather:", weather)
    print("Temperature:", temperature, "C")

    
else:
    print ("Error")

