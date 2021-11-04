birthday = input("Enter your bithday in DD-MM-YYYY format: " )
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

index = int(birthday[3:5]) - 1
bday_moth = months[index]

print ("You were born in " + bday_moth)
