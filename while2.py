import random
number = random.randint(0,10)

guess = int (input("I'm thinking a number 0-10. Can you guess it? "))

while True:
	if guess == number:
		break
	else:
		guess = int(input("Nope, Try again: "))

print("You Guessed it correctly, the number was", number)
