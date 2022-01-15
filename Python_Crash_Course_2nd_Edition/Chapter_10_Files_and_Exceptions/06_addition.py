number_1 = input("Please enter the first number: ")
number_2 = input("Please enter the second number: ")

try:
	number = int(number_1) + int(number_2)
except ValueError:
	print("Make sure both numbers you just entered are really numbers.")
else:
	print(f"The sum of them is {number}")