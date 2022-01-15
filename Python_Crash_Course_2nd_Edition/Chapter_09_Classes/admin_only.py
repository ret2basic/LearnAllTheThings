# For 9-12-multiple_module.py
from user import User
from privileges import Privileges

class Admin(User):

	def __init__(self, first_name, last_name, email, age):
		super().__init__(first_name, last_name, email, age)
		self.privilege = Privileges()