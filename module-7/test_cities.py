import unittest
from city_functions import format_city_country

class CitiesTestCase(unittest.TestCase) :
    """Tests for 'format_city_country.py'."""
    
    def test_city_country(self):
        city_location = format_city_country('athens', 'greece')
        self.assertEqual (city_location, 'Athens, Greece')
        
if __name__ == '__main__':
    unittest.main()
    
    