filename = 'guest.txt'

with open(filename, 'a') as fhand:
	guest = input("What's your name? ")
	fhand.write(guest + "\n")