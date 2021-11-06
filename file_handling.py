f = open("test.txt", "r") ## "r" means read
print (f.read())

f = open("test.txt", "w") ## "w" means write
f.write("This text will overwrite the content of our file")
f = open("test.txt")
print(f.read())

f = open("test.txt", "a") ## "a" means append
f.write("\nThis text will append to the file")
f = open("test.txt")
print (f.read())

f = open("test.txt", "r")