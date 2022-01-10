current_users = ['kali', 'mysql', 'JOHN', 'HEATH', 'admin']
new_users = ['coursera', 'edx', 'udemy', 'John', 'Heath']


current_users_lower = []
for user in current_users:
	current_users_lower.append(user.lower())

for user in new_users:
	if user.lower() in current_users_lower:
		print("This username is taken. Please enter a new username.")
	else:
		print("This username is available.")