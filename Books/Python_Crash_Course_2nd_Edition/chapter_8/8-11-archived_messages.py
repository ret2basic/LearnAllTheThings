def send_messages(messages, sent_messages):
	messages = list(reversed(messages))
	while messages:
		message = messages.pop()
		print(message)
		sent_messages.append(message)



messages = ['pwn is hard', 'reverse is hard', 'web is hard', 'crypto is hard', 'misc is hard']
sent_messages = []

send_messages(messages[:], sent_messages)

print("-----------------------------------------------------------------------------------")

print(messages)
print(sent_messages)


