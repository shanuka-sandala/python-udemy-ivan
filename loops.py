import random
colors = ["red","blue","green","yellow","black","white","purple"]

while True:
	taking_color = colors[random.randint(0,len(colors)-1)]
	guess = input("What is your guessing color: ")

	while True:
		if taking_color == guess.lower():
			break
		else:
			guess = input("Nope. Try again: ")	
	print("Correct! The color was ", taking_color)	

	play_again = input("Let's play again. Type 'no' to quit: ")

	if play_again.lower() == 'no':
		break

print("Game ended! thanks for playing.")