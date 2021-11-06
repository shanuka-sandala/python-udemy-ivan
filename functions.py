def say_hello():
	print("Hello!")

say_hello()

## The second example is more advanced by calling functions -->

def say_hello2(person):
	print("Hello! " + person + ", how are you doing?")

say_hello2("Shanuka")
say_hello2("Jayakodi")
say_hello2("Sandala")

## Another Example -->

def fahr2cel(fahr):
	cel = 5 * (fahr - 32) /9
	return cel

print("Celsius: ", round(fahr2cel(100),2))
print("Kelvin: ", round(fahr2cel(100) + 273.5 ,2))

## We can call many functions -->

def say_hello3(person1, person2 = "No one"):
	print("Hello! " + person1 + ", how are you doing? " + person2 + " is waiting for you.")

say_hello3("Julius","Caesar")
say_hello3("Julius")