import os
import requests


def get_weather_data(city):
    API_KEY = os.getenv('WEATHER_API_KEY')
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'temp': data['days'][0]['temp'],
            'conditions': data['days'][0]['conditions'],
            'humidity': data['days'][0]['humidity']
        }
    except requests.exceptions.RequestException as e:
        return {'error': f"Weather API error: {str(e)}"}
    except (KeyError, IndexError):
        return {'error': "Invalid city or data format"}