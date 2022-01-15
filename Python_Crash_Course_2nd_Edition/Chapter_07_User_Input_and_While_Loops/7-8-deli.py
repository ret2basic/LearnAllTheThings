sandwich_orders = ['tuna', 'turkey', 'beef', 'veggie']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"I made your {sandwich} sandwich")
	finished_sandwiches.append(sandwich)

print("\n")

print("I just made these sandwiches:")
for sandwich in finished_sandwiches:
	print(f"{sandwich.title()} sandwich")
