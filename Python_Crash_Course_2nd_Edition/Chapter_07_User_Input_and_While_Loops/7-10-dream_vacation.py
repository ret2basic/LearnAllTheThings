prompt = "\nIf you could visit one place in the world, where would you go? "
prompt += "\n(Enter 'quit' when you are finished.)"

places = []

while True:
	place = input(prompt)

	if place == 'quit':
		break
	else:
		places.append(place)

print("\nHere is the result of the poll:")
for place in places:
	print(place.title())
	
