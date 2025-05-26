import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

API_KEY = "0f5b9ca5cc0f1248fa7b23c2646d26d6"  # Replace with your active API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        print(f"\n{Fore.CYAN}{Style.BRIGHT}Weather in {city.capitalize()}:")
        print(f"{Fore.YELLOW}Temperature: {main['temp']}°C")
        print(f"{Fore.BLUE}Humidity: {main['humidity']}%")
        print(f"{Fore.MAGENTA}Condition: {weather['description'].capitalize()}")
    else:
        print(f"{Fore.RED}Error fetching weather data. Please check the city name or your API key.")

if __name__ == "__main__":
    print(f"{Fore.GREEN}{Style.BRIGHT}== Simple Weather App ==")
    city = input(f"{Fore.WHITE}Enter city name: ")
    get_weather(city)
