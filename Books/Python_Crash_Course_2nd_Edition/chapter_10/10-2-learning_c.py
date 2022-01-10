filename = 'learning_python.txt'

with open(filename) as fhand:
	lines = fhand.readlines()

for line in lines:
	print(line.replace('Python', 'C').rstrip())