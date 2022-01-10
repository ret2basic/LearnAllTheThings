pizzas = ['Pepperoni', 'Supreme', 'Cheese']
friend_pizzas = pizzas[:]

# Add a new item to each list
pizzas.append('Hawaiian')
friend_pizzas.append('Durian')

# Note that these two lists are different
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
	
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
