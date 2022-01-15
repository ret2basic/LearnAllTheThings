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

class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'vanilla', 'green tea', 'rocky road']

	def display_flavors(self):
		print("We have the following flavors available:")
		for flavor in self.flavors:
			print(flavor)


ice_cream_stand = IceCreamStand('iceiceice', 'ice cream')
ice_cream_stand.display_flavors()