# Class to get data from the OpenWeatherMap API

# Third-party imports
import requests
import pandas as pd
from datetime import datetime as dt


class WeatherData:
    def __init__(self, lat, lon, api_key):
        self.lat = lat
        self.lon = lon
        self.api_key = api_key
        self.lang = 'en'
        self.units = 'metric'
        self.exclude = 'minutely'
        self.url = f'https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&units={self.units}&exclude={self.exclude}&lang={self.lang}&appid={self.api_key}'

    def get_current_temp(self):
        weather = requests.get(self.url)

        if weather.status_code == 200:
            weather_data = weather.json()
            return weather_data['current']['temp']
        else:
            print('Could not get weather data. Status code:', weather.status_code)
            return None
        
    def get_temp_next_24h(self):
        weather = requests.get(self.url)

        if weather.status_code == 200:
            weather_data = weather.json()
            next24h_temp = []
            for i in weather_data['hourly'][1:25]:
                next24h_temp.append([dt.fromtimestamp(i['dt']), i['temp']])
            return next24h_temp
        else:
            print('Could not get weather data. Status code:', weather.status_code)
            return None
        
    def check_api_connection(self):
        # Make a minimal request to validate connection
        params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": self.api_key,
            "exclude": "minutely,hourly,daily,alerts"
        }
        response = requests.get(self.url, params=params)
        
        # Return the status code of the response
        return response.status_code
