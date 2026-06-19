
marks_of_student=[]
for i in range(15):
    a=int(input(f"Student {i+1}: "))
    marks_of_student.append(a)
marks_of_student.sort()
print()
print(marks_of_student)
print()
print(max(marks_of_student))
print()
print(min(marks_of_student))
print()
print(round(sum(marks_of_student)/len(marks_of_student)))

print()