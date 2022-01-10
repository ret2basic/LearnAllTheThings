# eXtensible Markup Language

## Quiz

### Question 1

What is "serialization" when we are talking about web services?

**Answer:**

- [x] The act of taking data stored in a program and formatting it so it can be sent across the network
- [ ] Sorting all the data stored in a tuple
- [ ] Making it so that dictionaries can maintain their keys in sorted order
- [ ] Marking each network packet so it can be put back into order on the receiving system

### Question 2

What is the method to cause Python to parse XML that is stored in a string?

**Answer:**

- [x] `fromstring()`
- [ ] `parse()`
- [ ] `readall()`
- [ ] `extract()`
- [ ] `xpath()`

### Question 3

In this XML, which are the "simple elements"?

```
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>
```

**Answer:**

- [ ] people
- [x] phone
- [ ] Noah
- [ ] person
- [x] name

**Note:**

- **Simple element** is a single node
- **Complex element** is a nested node containing one or more simple elements

### Question 4

In the following XML, which are attributes?

```
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
```

**Answer:**

- [ ] name
- [ ] person
- [ ] email
- [x] hide
- [x] type

### Question 5

In the following XML, which node is the parent node of node `e`

```
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```

**Answer:**

- [x] c
- [ ] e
- [ ] a
- [ ] b

### Question 6

Looking at the following XML, what text value would we find at path `/a/c/e`

```
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```

**Answer:**

- [ ] a
- [ ] b
- [ ] Y
- [x] Z
- [ ] e

### Question 7

What is the purpose of XML Schema?

**Answer:**

- [ ] A Python program to transform XML files
- [ ] To compute SHA1 checksums on data to make sure it is not modified in transit
- [x] To establish a contract as to what is valid XML
- [ ] To transfer XML data reliably during network outages

### Question 8

For this XML Schema:

```
<xs:complexType name=”person”>
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:integer"/>
    <xs:element name="dateborn" type="xs:date"/>
  </xs:sequence>
</xs:complexType>
```

And this XML,

```
<person>
   <lastname>Severance</lastname>
   <Age>17</Age>
   <dateborn>2001-04-17</dateborn>
</person>
```

Which tag is incorrect?

**Answer:**

- [ ] lastname
- [ ] dateborn
- [ ] age
- [ ] person
- [x] Age

### Question 9

What is a good time zone to use when computers are exchanging data over APIs?

**Answer:**

- [ ] The local time zone of the sending computer
- [ ] The local time zone of the sending computer without daylight savings time
- [ ] The local time zone of the receiving computer
- [ ] Universal Time / GMT

### Question 10

Which of the following dates is in ISO8601 format?

**Answer:**

- [ ] 2002-May-30
- [ ] 05/30/2002
- [x] 2002-05-30T09:30:10Z
- [ ] May 30, 2002

**Note:**

- 2002-05-30 => year-month-day
- T
- 09:30:10 => time of day
- Z => timezone, typically specified in UTC / GMT rather than local time zone.

## Programming Assignment: Extracting Data from XML

### Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
- Actual data: http://py4e-data.dr-chuck.net/comments_1266392.xml (Sum ends with 25)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

### Data Format and Approach

The data consists of a number of names and comment counts in XML as follows:

```xml
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
```

You are to look through all the `<comment>` tags and find the `<count>` values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

```python
counts = tree.findall('.//count')
```

Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
Sample Execution

```
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
```

### Implementation

```python
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
```