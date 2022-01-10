filename = 'guest_book.txt'

prompt = "What's your name? "
prompt += "(Press q when you finish) "

with open(filename, 'a') as fhand:
	while True:
		guest = input(prompt)

		if guest == 'q':
			break

		fhand.write(guest + "\n")