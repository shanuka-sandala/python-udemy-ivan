my_age = 22
stranger_age = int(input("What is your age: "))

if my_age > stranger_age:
	print ("I am older than you buddy!")

elif my_age < stranger_age:
	print ("You are older than me haha!")

elif my_age == stranger_age:
	print("Oh what a coincidence, we're on same age!")

else:
	print("This is out of range, it means unexpected error")