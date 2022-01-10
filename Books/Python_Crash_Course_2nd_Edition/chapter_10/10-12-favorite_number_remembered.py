import json

prompt = "What is your favorite number? "
filename = "favorite_number.json"

try:
	with open(filename) as fhand:
		number = json.load(fhand)
except FileNotFoundError:
	number = input(prompt)
	with open(filename, 'w') as fhand:
		json.dump(number, fhand)
		print("Cool! I just recorded your response.")
else:
	print(f"I know your favorite number! It's {number}.")