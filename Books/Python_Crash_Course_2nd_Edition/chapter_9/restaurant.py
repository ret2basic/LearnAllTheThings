# For 9-10-imported_restaurant.py
class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The name of the restaurant is {self.restaurant_name.title()}.")
		print(f"The cuisine type is {self.cuisine_type}.")

	def open_restaurant(self):
		print("The restaurant is open.")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, number):
		self.number_served += number