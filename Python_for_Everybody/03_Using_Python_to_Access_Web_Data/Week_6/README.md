# Quiz

## Question 1

Who is credited with getting the JSON movement started?

**Answer:**

- [ ] Pooja Sankar
- [ ] Mitchell Baker
- [ ] Bjarne Stroustrup
- [x] Douglas Crockford

## Question 2

Which of the following is true about an API?

**Answer:**

- [ ] An API defines the pin-outs for the USB connectors
- [ ] An API defines the header bits in the first 8 bits of all IP packets
- [ ] An API keeps servers running even when the power is off
- [x] An API is a contract that defines how to use a software library

## Question 3

Which of the following is a web services approach used by the Twitter API?

**Answer:**

- [ ] XML-RPC
- [x] REST
- [ ] SOAP
- [ ] CORBA

## Question 4

What kind of variable will you get in Python when the following JSON is parsed:

```json
[ "Glenn", "Sally", "Jen" ]
```

**Answer:**

- [x] A list with three items
- [ ] A dictionary with three key / value pairs
- [ ] A dictionary with one key / value pair
- [ ] Three tuples
- [ ] One tuple

## Question 5

Which of the following is not true about the service-oriented approach?

**Answer:**

- [ ] Standards are developed where many pairs of applications must work together
- [x] An application runs together all in one place
- [ ] Web services and APIs are used to transfer data between applications
- [ ] An application makes use of the services provided by other applications

## Question 6

Which of these two web service approaches is preferred in most modern service-oriented applications?

**Answer:**

- [x] REST - Representational state transfer
- [ ] SOAP - Simple Object Access Protocol

## Question 7

What library call do you make to append properly encoded parameters to the end of a URL like the following:

```
http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI
```

**Answer:**

- [ ] `re.match()`
- [ ] `urllib.urlcat()`
- [x] `urllib.parse.urlencode()`
- [ ] `re.encode()`

## Question 8

What happens when you exceed the Google geocoding API rate limit?

**Answer:**

- [ ] Your application starts to perform very slowly
- [x] You cannot use the API for 24 hours
- [ ] The API starts to perform very slowly
- [ ] You cannot use the API until you respond to an email that contains a survey question

## Question 9

What protocol does Twitter use to protect its API?

**Answer:**

- [ ] WS*Security
- [ ] PKI-HMAC
- [ ] SOAP
- [ ] SHA1-MD5
- [x] OAuth
- [ ] Java Web Tokens

## Question 10

What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?

**Answer:**

- [ ] content-type
- [ ] x-max-requests
- [ ] x-request-count-down
- [x] x-rate-limit-remaining

# Programming Assignment 1: Extracting Data from JSON

## Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
- Actual data: http://py4e-data.dr-chuck.net/comments_1266393.json (Sum ends with 70)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

## Data Format

The data consists of a number of names and comment counts in JSON as follows:

```json
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
```

The closest sample code that shows how to parse JSON and extract a list is [json2.py](https://www.py4e.com/code3/json2.py?PHPSESSID=6821de152ff8c3d0bdeae3b88f9389ce). You might also want to look at [geoxml.py](https://www.py4e.com/code3/geoxml.py?PHPSESSID=6821de152ff8c3d0bdeae3b88f9389ce) to see how to prompt for a URL and retrieve data from a URL.

## Sample Execution

```
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
```

## Implementation

```python
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
```

# Programming Assignment 2: Using the GeoJSON API

## Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first `place_id` from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

## API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

```
http://py4e-data.dr-chuck.net/json?
```

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.

To call the API, you need to include a `key=` parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the `urllib.parse.urlencode()` function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the `geojson` and `json` endpoints so make sure you are using the same end point as this autograder is using.

## Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a `place_id` of "ChIJLzabHQ7i2IgRzeZb_AgUj0Q".

```
$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2146 characters
Place id ChIJLzabHQ7i2IgRzeZb_AgUj0Q
```

## Implementation

```python

```