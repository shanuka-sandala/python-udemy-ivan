import requests
l = requests.get("https://opentdb.com/api.php?amount=10&category=23&difficulty=easy&type=multiple")
l.text
index = 0
import json
question = json.loads(l.text)

print("Please type 'quit' to exit the quiz. If you want to continue press enter")
user_answer = input("Input: ").lower

while user_answer != ("quit"):
    index = index + 1
    quiz = question['results'][index]['question']
    correct_ans = question['results'][index]['correct_answer']
    print(quiz)
    user_answer = input("Input: ")
    if correct_ans == user_answer:
    	print ("Correct! " + correct_ans + " was the correct answer!")
    else:
    	print("Nope, the answer was " + correct_ans)
    continue

print("Thanks for playing! Have a Good day!")
