blog_posts = ["","How to avoid Snake bites", "Do you want to be rich?", "", "PC Builds"]
for post in blog_posts:
	if post == "":
		continue
	else:
		print(post)

print ('----------------------------------')

myString = "This is a string"
for char in myString:
	print(char)

print ('----------------------------------')

for x in range(0,10):
	print(x)

print ('----------------------------------')

person = {'Name':'Shanuka', 'Age':22, 'Gender': 'Male'}
for key in person:
	print(key, ":", person[key])

print ('----------------------------------')

blog_posts = {"List1" : ["How to avoid Snake bites", "Do you want to be rich?", "PC Builds"], "List2" : ["Snake bites cures", "Expensive Trips", "Buy SSDs"]}
for category in blog_posts:
	print ("Posts about", category)
	for post in blog_posts[category]:
		print(post)

print ('----------------------------------')