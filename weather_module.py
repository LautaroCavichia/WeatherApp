import requests


def get_weather(city):
    api_key = 'e1765f54f86ee08cd4886bc77ef94a38'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    result = requests.get(base_url, params=params).json()

    if result.get('cod') == 200:
        temperature_kelvin = result['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Convert to Celsius
        description = result['weather'][0]['description']

        probability_of_rain = result.get('rain', {}).get('1h', 0)

        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Description: {description}")
        print(f"Probability of Rain (last 1 hour): {probability_of_rain} mm")
    else:
        error_message = result.get('message', 'Unknown error')
        print(f"Error: {error_message}")
