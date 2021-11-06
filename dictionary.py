person = {"name":"Shanuka", "gender":"Male", "age": 22, "address":"No.467/1E", "phone":"072555790"}
enter = input ("What information you want to get: " ).lower()
print(person.get (enter, "Invalid Property"))