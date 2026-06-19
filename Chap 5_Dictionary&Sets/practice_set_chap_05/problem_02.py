# Q.2 Write a program to input eight numbers from the user and display all the unique numbers (once).



# s=set()

# for i in range(8):
#     number=int(input(f"number {i+1}: "))
#     s.update({number})
# print(s)
"""we can use this code also but its formultiple entries ---> .update({})"""

s=set()

for i in range(8):
    number=int(input(f"number {i+1}: "))
    s.add(number)
print(s)
"""this one is better for single entry in a set --->.add()"""