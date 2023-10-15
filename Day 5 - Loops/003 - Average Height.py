# Don't change this code
student_heights = [150,180,124,140,170,160,150,164]
# Don't change this code
totalheight  = 0
totalstudents = 0
for i in student_heights:
    totalstudents += 1
    totalheight = totalheight + i

averageheight = totalheight / totalstudents
print(f"There are {totalstudents} students")
print(f"The average height of students is {averageheight:.2f}")