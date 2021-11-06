number = input("Enter a number: ")

try:
	number = float(number)
	print("The number is ", number)
except:
	print("Invalid Number input")