filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'

try:
	with open(filename_1) as file_1:
		cats = file_1.read()

	with open(filename_2) as file_2:
		dogs = file_2.read()
except FileNotFoundError:
	print("Some file is missing.")
else:
	print(cats)
	print(dogs)