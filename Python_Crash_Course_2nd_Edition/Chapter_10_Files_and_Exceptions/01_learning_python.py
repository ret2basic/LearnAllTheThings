filename = 'learning_python.txt'

# Variation 1
with open(filename) as fhand:
	contents = fhand.read()

print(contents)

print("----------------------------------------------")

# Variation 2
with open(filename) as fhand:
	for line in fhand:
		print(line.rstrip())

print("----------------------------------------------")

# Variation 3
with open(filename) as fhand:
	lines = fhand.readlines()

for line in lines:
	print(line.rstrip())

