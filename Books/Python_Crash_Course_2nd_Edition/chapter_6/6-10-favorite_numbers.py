favorite_numbers = {
	'root': [0, 1, 2], 
	'kali': [21, 22], 
	'apache': [80, 443], 
	'foo': [88, 99, 1010, 1111], 
	'bar': [233],
	}

for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(number)
	