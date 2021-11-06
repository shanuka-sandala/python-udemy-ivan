data_valid = False

while data_valid == False:
	grade1 = float(input("Grade 1 Marks: " ))
	if grade1 < 0 or grade1 > 10:
		print("Grade should be 0 and 10")
		continue
	else:
		data_valid = True

data_valid = False
while data_valid == False:
	grade2 = float(input("Grade 2 Marks: " ))
	if grade2 < 0 or grade2 > 10:
		print("Grade should be 0 and 10")
		continue
	else:
		data_valid = True

data_valid = False
while data_valid == False:
	total_classes = int(input("Number of classes: "))
	if total_classes <= 0:
		print("The number of classes cannot be 0 or less")
		continue
	else:
		data_valid = True

data_valid = False
while data_valid == False:
	absences = int(input("Number of absences: "))
	if absences < 0 or absences > total_classes:
		print("The number of absences cannot be less than 0 or greater than the number of total classes")
		continue
	else:
		data_valid = True

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