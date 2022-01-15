import unittest

class Employee:

	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, raise_amount=5000):
		self.annual_salary += raise_amount

class EmployeeTestCase(unittest.TestCase):

	def setUp(self):
		self.root = Employee('I am', 'root', 1000000)

	def test_give_default_raise(self):
		self.root.give_raise()
		self.assertEqual(self.root.annual_salary, 1005000)

	def test_give_custom_raise(self):
		self.root.give_raise(1000000)
		self.assertEqual(self.root.annual_salary, 2000000)

if __name__ == '__main__':
	unittest.main()
