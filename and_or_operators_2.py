print("Welcome to BMI calculator")

height = float(input("Please enter your height in Meters (m): "))
weight = float(input("Please enter your weight in Kilograms (kg): "))

BMI = round(weight / (height * height),2)

print("BMI value is: ", BMI)

if BMI < 18.5:
	print("Underweight")
elif BMI > 18.5 or BMI <= 24.9:
	print("Normal weight")
elif BMI > 24.9 or BMI <= 29.9:
	print("Overweight")
elif BMI >= 30:
	print("Obesity")
else:
	print("Unexpected Error") 
