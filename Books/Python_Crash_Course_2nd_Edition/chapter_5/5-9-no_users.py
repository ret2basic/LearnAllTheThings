usernames = ['kali', 'mysql', 'john', 'heath', 'admin']

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {username}, thank you for logging in again.")
else:
	print("We need to find some users!")

usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {username}, thank you for logging in again.")
else:
	print("We need to find some users!")
