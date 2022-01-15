import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
	"""Test Cases for city_functions.py"""

	def test_city_country(self):
		test_case = city_country('santiago', 'chile')
		self.assertEqual(test_case, 'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()