# pylint: disable=wrong-import-position, no-member
# I have no clue why pylint is throwing no-member error
"""
Tests accuracy of full sudoku solving functionality
"""
import unittest
import sys
import test_api
sys.path.append(".")

class test_cloudy_codes(unittest.TestCase):
    """Tests access of weather code .json"""
    def test_clear_code(self):
        """Tests Clear Sky Weather Code"""
        self.assertEqual(test_api.read_weather_code(0), "Clear Sky")
    def test_mainly_clear(self):
        """Tests Mainly Clear Sky Code"""
        self.assertEqual(test_api.read_weather_code(1), "Mainly Clear Sky")
    def test_partly_cloudy(self):
        """Tests Partly Cloudy"""
        self.assertEqual(test_api.read_weather_code(1), "Partly Cloudy")

if __name__== '__main__':
    unittest.main()