favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

people = ['edward', 'sarah', 'kali', 'root', 'john', 'heath']

for person in people:
	if person in favorite_languages:
		print(f"Hi {person.title()}, thank you for responding!")
	else:
		print(f"Hi {person.title()}, please take the poll.")