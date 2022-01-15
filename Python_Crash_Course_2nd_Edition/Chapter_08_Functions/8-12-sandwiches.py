def sandwhich(*args):
	print("Your sandwhich comes with:")
	for item in args:
		print(item)
	print("\n")

sandwhich('turkey', 'tomato', 'cucumber')
sandwhich('nothing')
sandwhich('creatine', 'vitamin', 'glutamine', 'caffeine')