prompt = "\nPlease enter your pizza toppings: "
prompt == "\n(Enter 'quit' when you are finished.)"

while True:
	topping = input(prompt)

	if topping == 'quit':
		print("Got you. We will make the pizza and deliver to you in 30 minutes.")
		break

	print(f"Okay, I will add {topping} to your pizza.")