pet_1 = {
	'kind': 'bunny',
	'owner': 'ch3ny4n6',
}

pet_2 = {
	'kind': 'tiger',
	'owner': 'John Hammond',
}

pet_3 = {
	'kind': 'bear',
	'owner': 'Heath Adams',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
	print(f"{pet['owner']} owns a {pet['kind']}.")
	