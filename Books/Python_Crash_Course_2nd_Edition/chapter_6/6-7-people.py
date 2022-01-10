person_1 = {
	'first name': 'Foo',
	'last name': 'Bar',
	'age': 88,
	'city': 'Los Angeles',
	}

person_2 = {
	'first name': 'Gordon',
	'last name': 'Freeman',
	'age': 25,
	'city': 'Black Mesa',
	}

person_3 = {
	'first name': 'John',
	'last name': 'Hammond',
	'age': 151,
	'city': 'Area 51',
	}

people = [person_1, person_2, person_3]

for person in people:
	print(f"\nHere is the information about {person['first name']}:")
	for key, value in person.items():
		print(f"{key.title()}: {value}")
