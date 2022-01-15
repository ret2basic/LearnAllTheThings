#!/usr/bin/env python3
import json

from urllib.request import urlopen

# Read json
url = "http://py4e-data.dr-chuck.net/comments_1266393.json"
json_data = urlopen(url).read()

# Parse json
info = json.loads(json_data)["comments"]

# Compute the sum
result = 0
for item in info:
	result += item["count"]

print(result)