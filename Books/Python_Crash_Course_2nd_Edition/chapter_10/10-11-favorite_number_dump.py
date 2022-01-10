import json

prompt = "What is your favorite number? "
filename = "favorite_number.json"

number = input(prompt)

with open(filename, 'w') as fhand:
	json.dump(number, fhand)
	print("Cool! I just recorded your response.")