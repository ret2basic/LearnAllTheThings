#!/usr/bin/env python3
import socket
import threading


"""
This is a standard multithreaded TCP server.
Run it together with tcp_client.py for testing.
"""


host = "0.0.0.0"
port = 9998


def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Set host and port for the listener
	server.bind((host, port))
	# Start listening with maximum connection 5
	server.listen(5)
	print(f"[*] Listening on {host}:{port}")

	while True:
		# Catch the connection request from the client
		client, address = server.accept()
		print(f"[*] Accepted connection from {address[0]}:{address[1]}")
		# Multithread
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()


def handle_client(client_socket):
	with client_socket as sock:
		request = sock.recv(1024)
		print(f"[*] Received: {request.decode('utf-8')}")
		sock.send(b"ACK")


if __name__ == "__main__":
	main()