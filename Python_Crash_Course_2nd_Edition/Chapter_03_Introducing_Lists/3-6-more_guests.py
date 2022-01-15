people = ['Newton', 'Einstein', 'Schrödinger']

print(f"Hi {people[0]}, would you like to have dinner with me?")
print(f"Hi {people[1]}, would you like to have dinner with me?")
print(f"Hi {people[2]}, would you like to have dinner with me?")
print(f"What? {people[2]} can't make it? Well, such a pity. Let's do this again.")

people[2] = 'Bohr'
print(f"Hi {people[0]}, would you like to have dinner with me?")
print(f"Hi {people[1]}, would you like to have dinner with me?")
print(f"Hi {people[2]}, would you like to have dinner with me?")
print("Hey guys, I found a bigger dinner table, so we can invite more people!")

people.insert(0, 'Tesla')
people.insert(2, 'Feynman')
people.append('Planck')

print(f"Hi {people[0]}, would you like to have dinner with me?")
print(f"Hi {people[1]}, would you like to have dinner with me?")
print(f"Hi {people[2]}, would you like to have dinner with me?")
print(f"Hi {people[3]}, would you like to have dinner with me?")
print(f"Hi {people[4]}, would you like to have dinner with me?")
print(f"Hi {people[5]}, would you like to have dinner with me?")