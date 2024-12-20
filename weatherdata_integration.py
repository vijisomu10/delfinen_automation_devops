"""
4.	Integrationstest som verifierar att API fungerar korrekt.
Integration tests will use actual API calls, 
so you’ll need a valid API key for OpenWeatherMap and internet connectivity.

Run: python -m unittest weatherdata_integration.py
 """

import unittest
import os
from dotenv import load_dotenv
from get_weather import WeatherData

class IntegrationTestWeatherDataAPIConnection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.api_key = os.getenv("api_key")
        cls.weather = WeatherData(lat=59.3293, lon=18.0686, api_key=cls.api_key)

    def test_api_connection_success(self):
        # Test to ensure API connection is successful
        response_status = self.weather.check_api_connection()

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response_status, 200)

if __name__ == '__main__':
    unittest.main()