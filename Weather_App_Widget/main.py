import os
import requests
from dotenv import load_dotenv

def get_weather(code, api_key):
    try:
        if code == 0:
            city,state,country = input("Enter {city,state,country} format: ").split(",") 
            location_responce = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=5&appid={api_key}").json()
            for each_loc in location_responce:
                if each_loc['country'] == country and each_loc['name'] == city and each_loc['state'] == state:
                    lat,lon = location_responce[0]['lat'], location_responce[0]['lon']
                    print(lat,lon)
                    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        elif code == 1:
            zip_code, country = input("Enter {zip_code,country_code} format: ").split(",")
            url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country}&appid={api_key}"


        weather_responce = requests.get(url)
        return weather_responce.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

if "__main__" == __name__:
    load_dotenv() # loads/ takes environment variables from .env
    open_weather_api_key = os.environ.get("WEATHER_API_KEY")

    city_or_zip = int(input("Enter 0 for {city, State, Country}\n1 for zip/postal code\nAny other character to quit"))
    weather_data = get_weather(code=city_or_zip, api_key=open_weather_api_key)

    if weather_data['cod'] != 404:
        coord = weather_data["coord"]
        main = weather_data["main"]
        weather = weather_data["weather"][0]
        wind = weather_data["wind"]
        clouds = weather_data["clouds"]
        sys = weather_data["sys"]

        # Instead of this ugly looking terminal output we can Tkinter GUI implement(Desktop app) or django interface(Web app)
        print("\nFormatted Weather Information:")
        print(f"City: {weather_data['name']}, {sys['country']}")
        print(f"Coordinates: Latitude {coord['lat']}, Longitude {coord['lon']}")
        print(f"Temperature: {main['temp']}°C (Feels like: {main['feels_like']}°C)")
        print(f"Min Temperature: {main['temp_min']}°C, Max Temperature: {main['temp_max']}°C")
        print(f"Weather: {weather['main']} - {weather['description'].capitalize()}")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind: {wind['speed']} m/s at {wind['deg']}° (Gusts up to {wind.get('gust', 'N/A')} m/s)")
        print(f"Cloudiness: {clouds['all']}%")
        print(f"Visibility: {weather_data.get('visibility', 'N/A')} meters")
        print(f"Sunrise: {sys['sunrise']}")
        print(f"Sunset: {sys['sunset']}")