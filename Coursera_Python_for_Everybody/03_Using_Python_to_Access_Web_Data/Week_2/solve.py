#!/usr/bin/env python3
import re

result = 0
with open("regex_sum_1266388.txt", "r") as f:
	for line in f:
		numbers_as_strings = re.findall("[0-9]+", line)
		numbers_as_ints = list(map(int, numbers_as_strings))
		result += sum(numbers_as_ints)
print(result)