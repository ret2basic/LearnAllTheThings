filename = 'poll.txt'

prompt = "Why do you like programming? "
prompt += "(Press q when you finish) "

with open(filename, 'a') as fhand:
	while True:
		reason = input(prompt)

		if reason == 'q':
			break

		fhand.write(reason + "\n")