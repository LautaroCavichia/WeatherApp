import requests


def get_weather(city):
    api_key = 'e1765f54f86ee08cd4886bc77ef94a38'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    result = requests.get(base_url, params=params).json()
    #result to consolelog
    print(result)
