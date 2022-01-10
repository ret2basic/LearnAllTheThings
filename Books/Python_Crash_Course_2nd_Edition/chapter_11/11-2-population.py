import unittest
from city_population import city_country

class CityTestCase(unittest.TestCase):
	"""Test Cases for city_functions.py"""

	def test_city_country(self):
		test_case = city_country('santiago', 'chile')
		self.assertEqual(test_case, 'Santiago, Chile')

	def test_city_country_population(self):
		test_case = city_country('santiago', 'chile', '5000000')
		self.assertEqual(test_case, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
	unittest.main()