import random
names = []

for x in range (0,8):
	new_name = input("Enter the names: ")
	names.append(new_name)

taking_random = random.randint(0,7)
random_person = names[taking_random]

print("Random Person is: ", random_person)