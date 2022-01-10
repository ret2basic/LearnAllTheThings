#!/usr/bin/env python3
import socket


"""
The UDP client implementation is very similar to the TCP server implementation.
The differences are:

1. UDP uses SOCK_DGRAM instead of SOCK_STREAM.
2. Unlike TCP, UDP is a connectionless protocol, so it doesn't have the connect() function.
3. UDP uses sendto()/recvfrom() instead of send()/recv()
"""


#--------Setup--------#

host = "127.0.0.1"
port = 9997

# AF_INET => IPv4 ; SOCK_DGRAM => UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#--------I/O--------#

client.sendto(b"AAABBBCCC", (host, port))
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()