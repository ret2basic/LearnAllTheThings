#!/usr/bin/env python3
import re

# Search for lines that start with "From" and have an @ sign
with open("mbox-short.txt", "r") as f:
	for line in f:
		line = line.rstrip()
		if re.search("^F..m:.+@", line):
			print(line)