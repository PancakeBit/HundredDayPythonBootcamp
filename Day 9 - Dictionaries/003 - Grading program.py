student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
# Don't change the code above

# Make a new dictionary and add the student's grades converted to new grading system
for student in student_scores:
    if student_scores[student] > 90:
        grade = "Outstanding"
    elif student_scores[student] > 80:
        grade = "Exceeds expectation"
    elif student_scores[student] > 70:
        grade = "Acceptable"
    else:
        grade = "Failed"
    student_grades[student] = grade

print(student_grades)
