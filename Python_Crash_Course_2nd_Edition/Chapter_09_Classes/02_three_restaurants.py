class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"The name of the restaurant is {self.restaurant_name.title()}.")
		print(f"The cuisine type is {self.cuisine_type}.")

	def open_restaurant(self):
		print("The restaurant is open.")

restaurant_1 = Restaurant('sushi ippo', 'sushi')
restaurant_2 = Restaurant('tantawan thai kitchen', 'Thai')
restaurant_3 = Restaurant('beijing tasty house', 'Chinese')

restaurant_1.describe_restaurant()
print("-----------------------------------------")
restaurant_2.describe_restaurant()
print("-----------------------------------------")
restaurant_3.describe_restaurant()