marks_of_student = []

for i in range(6):
    a=int(input(f"student {i+1}: "))
    marks_of_student.append(a)
marks_of_student.sort()
print(marks_of_student)


# marks_of_student = []

# for i in range(6):
#     # input(f"student {i+1}: ")             
#     marks_of_student.append(int(input(f"student {i+1}: "))) # for this we need to comment(ctrl+/) line above
#     marks_of_student.sort()
# print(marks_of_student)