import requests
from langchain.tools import tool
from src.config import OPENWEATHER_API_KEY

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    else:
        return f"Error fetching weather for {city}: {response.status_code}"