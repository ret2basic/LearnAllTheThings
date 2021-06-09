#!/usr/bin/env python3

def square(x):
	return x * x

primes = [2, 3, 5, 7, 11]

# Method 1: loop
result = []
for number in primes:
	result.append(square(number))

print(result)

# Method 2: map
print(list(map(square, primes)))

# Method 3: list comprehension
print([square(number) for number in primes])