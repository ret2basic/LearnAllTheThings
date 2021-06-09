#!/usr/bin/env python3

# Built-in function 1: max()
print(max([1, 2, 3, 4]))
print(max([1, 2, 3, 4], key=lambda x: x * x))

# Built-in function 2: min()
print(min([1, 2, 3, 4]))
print(min([1, 2, 3, 4], key=lambda x: x * x))

# Built-in function 3: any()
print(any([True, False]))
print(any([False, False]))

# Built-in function 4: all()
print(all([True, False]))
print(all([True, True]))