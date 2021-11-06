grade1 = float(input("Grade 1 Marks: " ))
grade2 = float(input("Grade 2 Marks: " ))
absences = int(input("Number of absences: "))
total_classes = int(input("Number of classes: "))

avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round(attendance * 100,2))+'%')

if avg_grade >= 6:
	if attendance >= 0.8:
		print("You Passed with '80%' attendance")
	elif attendance < 0.8:
		print("You are not passed because you have not '80%' attendance")
	else:
		print("Error!")

elif avg_grade < 6:
	if attendance >= 0.8:
		print("You are not passed, but you have '80%' attendance")
	elif attendance < 0.8:
		print("You are not passed also you have not '80%' attendance")
	else:
		print("Error!")

else:
	print("Error2")