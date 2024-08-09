# Weather App

This is a simple Python script that fetches weather data using the OpenWeatherMap API. It allows users to retrieve current weather information based on a city, state or a ZIP/postal code along with country combination.

## Features

- Fetch weather data using a city, state, and country combination.
- Fetch weather data using a ZIP/postal code.
- Displays formatted weather information, including temperature, humidity, wind speed, and more.

## Prerequisites

Before running this script, you need to have the following:

1. Python 3.x installed on your system.
2. `requests` library: You can install it using `pip install requests`.
3. `python-dotenv` library: You can install it using `pip install python-dotenv`.
4. An API key from OpenWeatherMap: You can get it by signing up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

## Setup

1. Clone or download the repository to your local machine.

2. Navigate to the project directory.

3. Create a `.env` file in the root directory of the project, and add your OpenWeatherMap API key like so:

    ```env
    WEATHER_API_KEY=your_openweathermap_api_key_here
    ```

4. Install the required dependencies:

    ```bash
    pip install requests python-dotenv
    ```

## Usage

1. Run the script:

    ```bash
    python weather_app.py
    ```

2. Choose the type of input:

    - Enter `0` to search weather by `{city, state, country}` format.
    - Enter `1` to search weather by `{zip_code, country_code}` format.
    - Enter any other character to quit the program.

3. If you chose `0`, enter the city, state, and country in the format `city,state,country` (e.g., `Los Angeles,California,US` or `Buffalo,New York,US`).

4. If you chose `1`, enter the ZIP/postal code and country code in the format `zip_code,country_code` (e.g., `90001,US` or `20171`).

5. The script will fetch and display the current weather data in a formatted output.

## Example Output

```plaintext
Enter 0 for {city, State, Country}
1 for zip/postal code
Any other character to quit: 0

Enter {city,state,country} format: Los Angeles,CA,US

Formatted Weather Information:
City: Los Angeles, US
Coordinates: Latitude 34.0522, Longitude -118.2437
Temperature: 295.15°C (Feels like: 294.15°C)
Min Temperature: 293.71°C, Max Temperature: 297.04°C
Weather: Clear - Clear sky
Pressure: 1015 hPa
Humidity: 53%
Wind: 1.54 m/s at 350° (Gusts up to N/A m/s)
Cloudiness: 1%
Visibility: 10000 meters
Sunrise: 1694254200
Sunset: 1694299200
```

## Error Handling
The script includes basic error handling to catch and display errors related to:

- HTTP errors
- Connection errors
- Timeout errors
- Other request exceptions

## Future Improvements
- Add a graphical user interface (GUI) using Tkinter or a web interface using Django or Flask.
- Improve error handling and validation for user inputs.
- Display sunrise and sunset times in a human-readable format.