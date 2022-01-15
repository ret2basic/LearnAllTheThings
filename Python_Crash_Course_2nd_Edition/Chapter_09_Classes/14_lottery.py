from random import choice

pool = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']

lottery = ""
for _ in range(4):
	lottery += choice(pool)

print(f"Any ticket matching {lottery} wins a prize!")