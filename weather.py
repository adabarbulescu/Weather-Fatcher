import requests

API_KEY = "62372f09025c7302bd7189cdc93125d0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]['description']
    temperature = round(data["main"]["temp"] - 273.15)
    feels_like = round(data['main']['feels_like'] - 273.15)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
    print("It feels like: ", feels_like, "celsius")
else:
    print("An error occured.")
