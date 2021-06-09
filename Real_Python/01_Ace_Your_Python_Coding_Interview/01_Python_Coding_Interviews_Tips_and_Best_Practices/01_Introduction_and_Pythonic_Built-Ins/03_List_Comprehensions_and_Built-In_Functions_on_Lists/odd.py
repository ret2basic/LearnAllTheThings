#!/usr/bin/env python3

def is_odd(x):
    return x % 2 == 1
    
primes = [2, 3, 5, 7, 11]

# Method 1: filter
print(list(filter(is_odd, primes)))

# Method 2: list comprehension
print([num for num in primes if is_odd(num)])