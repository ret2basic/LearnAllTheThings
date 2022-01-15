from restaurant import Restaurant

class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'vanilla', 'green tea', 'rocky road']

	def display_flavors(self):
		print("We have the following flavors available:")
		for flavor in self.flavors:
			print(flavor)


restaurant = Restaurant('sushi ippo', 'sushi')
restaurant.describe_restaurant()