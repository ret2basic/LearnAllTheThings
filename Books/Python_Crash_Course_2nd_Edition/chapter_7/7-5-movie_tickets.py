prompt = "\nPlease enter your age: "
prompt == "\n(Enter 'quit' when you are finished.)"

while True:
	age = input(prompt)

	if age == 'quit':
		print("Bye!")
		break

	age = int(age)

	if age < 3:
		print("Your ticket is free.")
	elif 3 <= age <= 12:
		print("Your ticket is $10.")
	elif age > 12:
		print("Your ticket is $15.")