import requests


def get_city_suggestions(prefix):
    username = 'lauta13'
    base_url = 'http://api.geonames.org/searchJSON'
    params = {'name_startsWith': prefix, 'maxRows': 10, 'username': username}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        print(f"Success: {response.status_code}")
        data = response.json()
        cities = [place['name'] for place in data.get('geonames', [])]
        print(cities)
        return cities

    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return []
