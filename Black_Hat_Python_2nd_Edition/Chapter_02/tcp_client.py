#!/usr/bin/env python3
import socket


"""
This is a quick-and-dirty TCP client with the following 3 assumptions:

1. The connection will aways succeed.
2. The server expects us to send data first.
3. The server will always return data to us in a timely fashion.
"""


#--------Setup--------#

host = "0.0.0.0"
port = 9998

# AF_INET => IPv4 ; SOCK_STREAM => TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

#--------I/O--------#

client.send(b"1337")
response = client.recv(4096)

print(response.decode())
client.close()