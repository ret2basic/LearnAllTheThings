glossary = {
	'boolean': 'True or False.',
	'tuple': 'An immutable list.',
	'format string': 'Use variable in a string.',
	'conditional test': 'A statement that returns True or False.',
	'integer division': "A type of division that drops the fractional part.",
	'set': 'A collection in which each item must be unique.',
	'dictionary': 'A data structure that stores key-value pairs.',
}

for term, definition in glossary.items():
	print(f"\n{term.title()}: {definition}")