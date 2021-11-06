import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("Type the word 'programming' as fast you can for five times!")
input("Press enter to continue.")

while len(times) < 5:
	start = t.time()
	word = input("Type the word: ")
	end = t.time()
	time_elapsed = end - start

	times.append(time_elapsed)

	if (word.lower() != "programming"):
		mistakes += 1

print("You made "+ str(mistakes) + " mistake(s)")
print("Let's see your evoluation")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel('Times in seconds')
plt.xlabel('Attempts')
plt.title('Typing Evolution')
plt.show()
