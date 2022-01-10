#!/usr/bin/env python3
import xml.etree.ElementTree as ET

from urllib.request import urlopen

# Read xml
url = "http://py4e-data.dr-chuck.net/comments_1266392.xml"
xml = urlopen(url).read()

# Parse xml
stuff = ET.fromstring(xml)
lst = stuff.findall("comments/comment")

# Compute the sum
result = 0
for item in lst:
	result += int(item.find("count").text)

print(result)