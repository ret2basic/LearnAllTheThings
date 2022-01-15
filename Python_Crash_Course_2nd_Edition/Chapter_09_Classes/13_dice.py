from random import randint

class Die:

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print(randint(1, self.sides))

die_1 = Die()

for _ in range(10):
	die_1.roll_die()

print("-----------------------------")

die_2 = Die(10)
die_3 = Die(20)

for _ in range(10):
	die_2.roll_die()

print("-----------------------------")

for _ in range(10):
	die_3.roll_die()