# Networks and Sockets

## Quiz

### Question 1

What do we call it when a browser uses the HTTP protocol to load a file or page from a server and display it in the browser?

**Answer:**

- [ ] DECNET
- [ ] SMTP
- [x] The Request/Response Cycle
- [ ] IMAP
- [ ] Internet Protocol (IP)

### Question 2

Which of the following is most similar to a TCP port number?

**Answer:**

- [ ] A street number in an address
- [ ] The GPS coordinates of a building
- [ ] The distance between two locations
- [ ] A telephone number
- [x] A telephone extension

### Question 3

What must you do in Python before opening a socket?

**Answer:**

- [x] import socket
- [ ] open socket
- [ ] \_socket = true
- [ ] import tcp-socket
- [ ] import tcp

### Question 4

In a client-server application on the web using sockets, which must come up first?

**Answer:**

- [x] server
- [ ] client
- [ ] it does not matter

### Question 5

Which of the following is most like an open socket in an application?

**Answer:**

- [x] An "in-progress" phone conversation
- [ ] Fiber optic cables
- [ ] The wheels on an automobile
- [ ] The chain on a bicycle
- [ ] The ringer on a telephone

### Question 6

What does the "H" of HTTP stand for?

**Answer:**

- [ ] Simple
- [ ] Manual
- [ ] Hyperspeed
- [x] HyperText
- [ ] wHolsitic

### Question 7

What is an important aspect of an Application Layer protocol like HTTP?

**Answer:**

- [ ] What is the IP address for a domain like www.dr-chuck.com?
- [ ] How much memory does the server need to serve requests?
- [ ] How long do we wait before packets are retransmitted?
- [x] Which application talks first?  The client or server?

### Question 8

What are the three parts of this URL (Uniform Resource Locator)?

```
http://www.dr-chuck.com/page1.htm
```

**Answer:**

- [ ] Page, offset, and count
- [ ] Host, offset, and page
- [ ] Protocol, document, and offset
- [x] Protocol, host, and document
- [ ] Document, page, and protocol

### Question 9

When you click on an anchor tag in a web page like below, what HTTP request is sent to the server?

```
<p>Please click <a href="page1.htm">here</a>.</p>
```

**Answer:**

- [x] GET
- [ ] POST
- [ ] PUT
- [ ] DELETE
- [ ] INFO

### Question 10

Which organization publishes Internet Protocol Standards?

**Answer:**

- [ ] SIFA
- [ ] IMS
- [x] IETF
- [ ] SCORM
- [ ] LDAP

## Programming Assignment: Understanding the Request / Response Cycle

**Exploring the HyperText Transport Protocol**

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt

There are three ways that you might retrieve this web page and look at the response headers:

Preferred: Modify the [socket1.py](https://www.py4e.com/code3/socket1.py?PHPSESSID=43c2e1eb240e0ad8e0c09f7125f07e05) program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Enter the header values in each of the fields below and press "Submit".

Last-Modified: Content-Type:
ETag: "1d3-54f6609240717"
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Content-Type: text/plain