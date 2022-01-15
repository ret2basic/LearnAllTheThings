while True:
	number_1 = input("Please enter the first number: (Press q to quit) ")
	if number_1 == 'q':
		break 

	number_2 = input("Please enter the second number: (Press q to quit) ")
	if number_2 == 'q':
		break

	try:
		number = int(number_1) + int(number_2)
	except ValueError:
		print("Make sure both numbers you just entered are really numbers.")
	else:
		print(f"The sum of them is {number}")