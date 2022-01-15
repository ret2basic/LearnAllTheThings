# Regular Expression

## Quiz

### Question 1

Which of the following best describes "Regular Expressions"?

**Answer:**

- [ ] A way to solve Algebra formulas for the unknown value
- [ ] A way to calculate mathematical values paying attention to operator precedence
- [x] A small programming language unto itself
- [ ] The way Python handles and recovers from errors that would otherwise cause a traceback

### Question 2

What will the `\$` regular expression match?

**Answer:**

- [ ] An empty line
- [x] A dollar sign
- [ ] A new line at the end of a line
- [ ] The beginning of a line
- [ ] The end of a line

### Question 3

What would the following mean in a regular expression? `[a-z0-9]`

**Answer:**

- [ ] Match an entire line as long as it is lowercase letters or digits
- [x] Match a lowercase letter or a digit
- [ ] Match anything but a lowercase letter or digit
- [ ] Match any number of lowercase letters followed by any number of digits
- [ ] Match any text that is surrounded by square braces

### Question 4

What is the type of the return value of the `re.findall()` method?

**Answer:**

- [ ] A string
- [x] A list of strings
- [ ] A single character
- [ ] A boolean
- [ ] An integer

### Question 5

What is the "wild card" character in a regular expression (i.e., the character that matches any character)?

**Answer:**

- [x] `.`
- [ ] `*`
- [ ] `$`
- [ ] `?`
- [ ] `+`
- [ ] `^`

### Question 6

What is the difference between the `+` and `*` character in regular expressions?

**Answer:**

- [x] The `+` matches at least one character and the `*` matches zero or more characters
- [ ] The `+` matches upper case characters and the `*` matches lowercase characters
- [ ] The `+` matches the beginning of a line and the `*` matches the end of a line
- [ ] The `+` matches the actual plus character and the `*` matches any character
- [ ] The `+` indicates "start of extraction" and the `*` indicates the "end of extraction"

### Question 7

What does the `[0-9]+` match in a regular expression?

**Answer:**

- [ ] Any number of digits at the beginning of a line
- [ ] Zero or more digits
- [ ] Any mathematical expression
- [x] One or more digits
- [ ] Several digits followed by a plus sign

### Question 8

What does the following Python sequence print out?

```python
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
```

**Answer:**

- [ ] `['From:']`
- [ ] `From:`
- [ ] `:`
- [ ] `^F.+:`
- [x] `['From: Using the :']`

### Question 9

What character do you add to the `"+"` or `"*"` to indicate that the match is to be done in a non-greedy manner?

**Answer:**

- [ ] `$`
- [ ] `^`
- [x] `?`
- [ ] `\g`
- [ ] `**`
- [ ] `++`

### Question 10

Given the following line of text:

```
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```

What would the regular expression `'\S+?@\S+'` match?

**Answer:**

- [x] `stephen.marquard@uct.ac.za`
- [ ] `From`
- [ ] `\@\`
- [ ] `d@uct.ac.za`
- [ ] `marquard@uct`

## Programming Assignment: Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

### Data Files

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1266388.txt (There are 85 values and the sum ends with 172)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

### Data Format

The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

```
Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...
```

The sum for the sample text above is **27486**. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

### Handling The Data

The basic outline of this problem is to read the file, look for integers using the `re.findall()`, looking for a regular expression of `'[0-9]+'` and then converting the extracted strings to integers and summing up the integers.

### Optional: Just for Fun

There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

```
Python 2
import re
print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

Python 3:
import re
print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
```

Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

### Implementation

```python
#!/usr/bin/env python3
import re

result = 0
with open("regex_sum_1266388.txt", "r") as f:
	for line in f:
		numbers_as_strings = re.findall("[0-9]+", line)
		numbers_as_ints = [int(number_as_string) for number_as_string in numbers_as_strings]
		result += sum(numbers_as_ints)

print(result)
```