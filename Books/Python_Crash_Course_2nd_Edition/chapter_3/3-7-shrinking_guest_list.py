guests = ['Newton', 'Einstein', 'Schrödinger']

print(f"Hi {guests[0]}, would you like to have dinner with me?")
print(f"Hi {guests[1]}, would you like to have dinner with me?")
print(f"Hi {guests[2]}, would you like to have dinner with me?")
print(f"What? {guests[2]} can't make it? Well, such a pity. Let's do this again.")

guests[2] = 'Bohr'

print(f"Hi {guests[0]}, would you like to have dinner with me?")
print(f"Hi {guests[1]}, would you like to have dinner with me?")
print(f"Hi {guests[2]}, would you like to have dinner with me?")
print("Hey guys, I found a bigger dinner table, so we can invite more guests!")

guests.insert(0, 'Tesla')
guests.insert(2, 'Feynman')
guests.append('Planck')

print(f"Hi {guests[0]}, would you like to have dinner with me?")
print(f"Hi {guests[1]}, would you like to have dinner with me?")
print(f"Hi {guests[2]}, would you like to have dinner with me?")
print(f"Hi {guests[3]}, would you like to have dinner with me?")
print(f"Hi {guests[4]}, would you like to have dinner with me?")
print(f"Hi {guests[5]}, would you like to have dinner with me?")
print("Oh man, the dinner table won't arrive on time. Now I can only invite guests. Sorry guys.")

person = guests.pop()
print(f"Sorry {person}, I can't invite you this time. I will buy you lunch when I see you.")
person = guests.pop()
print(f"Sorry {person}, I can't invite you this time. I will buy you lunch when I see you.")
person = guests.pop()
print(f"Sorry {person}, I can't invite you this time. I will buy you lunch when I see you.")
person = guests.pop()
print(f"Sorry {person}, I can't invite you this time. I will buy you lunch when I see you.")

print(f"Hi {guests[0]}, you are still invited. See you tonight!")
print(f"Hi {guests[1]}, you are still invited. See you tonight!")

del guests[1]
del guests[0]
print(guests)
