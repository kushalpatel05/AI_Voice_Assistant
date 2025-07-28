from voice import speak             # Custom Module
import requests                     # For making HTTP API requests (weather, news)
from dotenv import load_dotenv      # used to load environment variables from a .env file into your program's environment. 
import os

# Weather Information using OpenWeatherMap API
def get_weather(city):

    load_dotenv()
    weather_api = os.getenv("WEATHER_API_KEY")   # Your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,               # City name
        'appid': weather_api,    # API key
        'units': 'metric'        # To get temprature in Celsius
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] == 200:     # SUccess
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            report = (
                f"The current weather in {city} is {weather} with a temperature of {temp}°C, "
                f"humidity of {humidity}% and wind speed of {wind} m/s."
            )
            speak(report)
        else:
            speak("Sorry, I couldn't find weather information for that location.")
    except Exception as e:
        speak("Sorry, something went wrong while getting the weather.")
        print("Error:", e)