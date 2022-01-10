sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'beef', 'pastrami', 'veggie']
finished_sandwiches = []

print("The deli has run out of pastrami, sorry.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"I made your {sandwich} sandwich")
	finished_sandwiches.append(sandwich)

print("\n")

print("I just made these sandwiches:")
for sandwich in finished_sandwiches:
	print(f"{sandwich.title()} sandwich")
