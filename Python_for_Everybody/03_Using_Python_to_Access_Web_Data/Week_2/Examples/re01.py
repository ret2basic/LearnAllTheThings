#!/usr/bin/env python3
import re

# Search for lines that contain "From"
with open("mbox-short.txt", "r") as f:
	for line in f:
		line = line.rstrip()
		if re.search("From:", line):
			print(line)