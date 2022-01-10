rivers = {
	'amazon river': 'colombia',
	'nile': 'egypt',
	'Yangtze River': 'china',
}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")