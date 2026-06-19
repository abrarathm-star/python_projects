l1=[2,6,20.5,15,22,59,24,44,40,89,199,343.56]
l2=[2,3,29,4,22,33,24,77,40,89,184,343]


# sort()

l1.sort()
l2.sort()
print(l1)
print(l2)



# reverse()

l1.reverse()
print(l1)       

l2.reverse()
print(l2)



# sort() reverse()

l1.sort()
l1.reverse()
print(l1)                   # output ---> [343.56, 199, 89, 59, 44, 40, 24, 22, 20.5, 15, 6, 2] sorted and reversed.

"""or we can do"""

l1.sort(reverse=True)
print(l1)                   # output ---> [343.56, 199, 89, 59, 44, 40, 24, 22, 20.5, 15, 6, 2] sorted and reversed.



l2.sort()
l2.reverse()
print(l2)                   # ouput ---> [343, 184, 89, 77, 40, 33, 29, 24, 22, 4, 3, 2] sorted and reversed.

"""or we can do"""

l2.sort(reverse=True)
print(l2)                   # ouput ---> [343, 184, 89, 77, 40, 33, 29, 24, 22, 4, 3, 2] sorted and reversed.



# l1[1] = "abrar"
# print(l1)
# l1.sort()
# print(l1)                 #it shows error ---> TypeError: '<' not supported between instances of 'str' and 'int'



# append()

l1.append(7)                  # adds 7 at the end of the list      
print(l1)                     # ouput ---> [2, 6, 20.5, 15, 22, 59, 24, 44, 40, 89, 199, 343.56, 7]

l2.append(13)                 # adds 13 at the end of the list 
print(l2)                     # output ---> [2, 3, 29, 4, 22, 33, 24, 77, 40, 89, 184, 343, 13]



# sort() reverse() append()

l1.sort(reverse=True)
l1.append(10)
print(l1)                      # output ---> [343.56, 199, 89, 59, 44, 40, 24, 22, 20.5, 15, 6, 2, 10] 1.sorted, 2.revrsed, 3.appended

l1.sort()
l1.append(10)
l1.reverse()
print(l1)                        # output ---> [10, 343.56, 199, 89, 59, 44, 40, 24, 22, 20.5, 15, 6, 2] 1.sorted, 2. appended, 3. reversed

"""Sequence matters"""



# Insert()

l1.insert(5,18)
print(l1)                        # output ---> [10, 343.56, 199, 89, 59, 18, 40, 24, 22, 20.5, 15, 6, 2], 18 is inserted at index position [5]

l2.insert(3,0)
print(l2)                        # output ---> [343, 184, 89, 0, 77, 40, 33, 29, 24, 22, 4, 3, 2, 13],  0 is inserted at index position [3]



# pop()             

x=l1.pop(7)                      # Will delete element at index 7 and return its value.
print(l1)                        # [10, 343.56, 199, 89, 59, 18, 44, 24, 22, 20.5, 15, 10, 7, 6, 2]
print(x)                         #  40


y=l2.pop(12)                     # [343, 184, 89, 0, 77, 40, 33, 29, 24, 22, 4, 3, 13]
print(l2)                        # 2
print(y)                         # Will delete element at index 12 and return its value.



# remove()

l1.remove(44)
print(l1)                        # [10, 343.56, 199, 89, 59, 18, 24, 22, 20.5, 15, 10, 7, 6, 2]

"""44 is not the index,it is the actual value = 44"""