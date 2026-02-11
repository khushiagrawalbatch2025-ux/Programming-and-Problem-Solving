marks = list(map(int, input().split()))
total_marks = sum(marks)
print(total_marks)
percentage = total_marks / 4
print(f"{percentage:.2f}")
if percentage >= 75:
	grade = "Distinction"
elif percentage >= 40 and percentage < 50:
	grade = "Third Division"
elif percentage >= 50 and percentage < 60:
	grade = "Second Division"
elif percentage >= 60 :
	grade = "First Division"
else:
	grade = "Fail"
print(grade)
