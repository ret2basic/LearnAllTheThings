class User:

	def __init__(self, first_name, last_name, email, age):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.age = age

	def describe_user(self):
		print(f"The first name is {self.first_name.title()}")
		print(f"The last name is {self.last_name.title()}")
		print(f"The email is {self.email}")
		print(f"The age is {self.age}")

	def greet_user(self):
		print(f"Hi {self.first_name.title()}, how is it going?")

user_1 = User('John', 'Hammond', 'jhammond@gmail.com', '80')
user_2 = User('foo', 'bar', 'foobar@gmail.com', '23')
user_3 = User('kali', 'kali', 'kali@gmail.com', '233')

user_1.describe_user()
user_1.greet_user()
print("-----------------------------------------")
user_2.describe_user()
user_2.greet_user()
print("-----------------------------------------")
user_3.describe_user()
user_3.greet_user()
