"""
From Project Description
5.	Unit-test som säkerställer att databehandlingen ger förväntat resultat.
5.  Unit tests that ensure that data processing produces expected results.

Unit Testing:
We’ll use mocking to simulate responses from the OpenWeatherMap API 
so that our tests are faster and don’t rely on network connectivity.
Explanation:
Mocking with patch: 
We use @patch('requests.get') to replace requests.get with a mock object, simulating API responses.
Testing Method Outputs:
In test_get_current_temp, 
    we check that the mocked current temperature is returned correctly.
In test_get_temp_next_24h, 
    we verify that the function returns 24 temperature entries for the next 24 hours, 
    with each entry formatted as a list containing a timestamp and temperature. 

Run Unit Test in bash as:  python -m unittest testing.weatherdata_unit.py
"""

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime as dt
from get_weather import WeatherData  # Ensure your main script is named `weather_data.py`

class TestWeatherData(unittest.TestCase):

    @patch('requests.get')
    def test_get_current_temp(self, mock_get):
        # Mock response with a sample temperature value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'current': {'temp': 15.5}
        }
        mock_get.return_value = mock_response

        # Initialize WeatherData with test parameters
        weather = WeatherData(lat=59.3293, lon=18.0686, api_key="test_key")
        current_temp = weather.get_current_temp()

        # Check that the temperature returned matches the mocked data
        self.assertEqual(current_temp, 15.5)
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_temp_next_24h(self, mock_get):
        # Mock response with 24 hours of sample temperature data
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'hourly': [{'dt': 1609459200 + i * 3600, 'temp': float(10 + i)} for i in range(25)]
        }
        mock_get.return_value = mock_response

        # Initialize WeatherData and call the method
        weather = WeatherData(lat=59.3293, lon=18.0686, api_key="test_key")
        next24h_temp = weather.get_temp_next_24h()

        # Check that the data returned is in the expected format and length
        self.assertEqual(len(next24h_temp), 24)
        for hour_data in next24h_temp:
            self.assertIsInstance(hour_data[0], dt)  # timestamp as datetime
            self.assertIsInstance(hour_data[1], float)  # temperature as float
        mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()