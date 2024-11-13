"""
4.	Integrationstest som verifierar att API fungerar korrekt.
Integration tests will use actual API calls, 
so you’ll need a valid API key for OpenWeatherMap and internet connectivity.


Run: python -m unittest testing/weatherdata_integration.py
 """

import unittest
import os
from dotenv import load_dotenv
from datetime import datetime 
from get_weather import WeatherData

class IntegrationTestWeatherData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.api_key = os.getenv("api_key")
        cls.weather = WeatherData(lat=59.3293, lon=18.0686, api_key=cls.api_key)

    def test_integration_get_current_temp(self):
        # Call the actual API
        current_temp = self.weather.get_current_temp()

        # Assert that we get a float temperature value back
        self.assertIsInstance(current_temp, float)

    def test_integration_get_temp_next_24h(self):
        # Call the actual API
        next24h_temp = self.weather.get_temp_next_24h()

        # Assert that we get 24 records, each with a datetime and temperature
        self.assertEqual(len(next24h_temp), 24)
        for hour_data in next24h_temp:
            self.assertIsInstance(hour_data[0], datetime)  # Use datetime instead of dt
            self.assertIsInstance(hour_data[1], float)

if __name__ == '__main__':
    unittest.main()