# For 9-11-imported_admin.py
class User:

	def __init__(self, first_name, last_name, email, age):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		print(f"The first name is {self.first_name.title()}")
		print(f"The last name is {self.last_name.title()}")
		print(f"The email is {self.email}")
		print(f"The age is {self.age}")

	def greet_user(self):
		print(f"Hi {self.first_name.title()}, how is it going?")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Privileges():

	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user', 'can access database']

	def show_privileges(self):
		print("Admin has the following privileges:")
		for privilege in self.privileges:
			print(privilege)

class Admin(User):

	def __init__(self, first_name, last_name, email, age):
		super().__init__(first_name, last_name, email, age)
		self.privilege = Privileges()