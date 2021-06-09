#!/usr/bin/env python3

num_rows = 2
num_columns = 3

# Method 1: loop
grid = []
for _ in range(num_rows):
	curr_row = []
	for _ in range(num_columns):
		curr_row.append(0)
	grid.append(curr_row)

print(grid)

# Method 2: list comprehension
grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

print(grid)