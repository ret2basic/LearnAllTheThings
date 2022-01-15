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

restaurant = Restaurant('sushi ippo', 'sushi')
print(restaurant.number_served)

# Set directly
restaurant.number_served = 2
print(restaurant.number_served)

# Set by calling method
restaurant.set_number_served(4)
print(restaurant.number_served)

# Increment by calling method
restaurant.increment_number_served(800)
print(restaurant.number_served)