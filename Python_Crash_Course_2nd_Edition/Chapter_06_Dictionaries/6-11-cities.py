cities = {
	'Tokyo': {'country': 'Japan', 'population': 9_273_000, 'fact': 'nice food'},
	'Bangkok': {'country': 'Thailand', 'population': 8_281_000, 'fact': 'nice food'},
	'Seattle': {'country': 'Thailand', 'population': 724_745, 'fact': 'okay food'},
}

for city, info in cities.items():
	print(f"\nHere are some information about {city}:")
	for key, value in info.items():
		print(f"{key}: {value}")
