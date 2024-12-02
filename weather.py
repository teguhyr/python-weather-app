import requests

API_KEY = "9e4cb90e600975b236981582f8852b7f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        return f"The weather in {city} is {description} with a temperature of {temperature}°C and humidity of {humidity}%."
    else:
        return "City not found or API request failed."

if __name__ == "__main__":
    city = input("Enter the city name: ")
    print(get_weather(city))




