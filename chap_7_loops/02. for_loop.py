# print 1 - 20

for i in range(1,21):
    print(i)
print()



# print even number 

for i in range(2,21,2):         # this third value 2 means jumpby 2
    print(i)
print()



# Table of 5

for i in range(1,11):
    print(f"5 x {i} =",5*i)
print()



# print your name 5 times

for i in range(5):
    print("abrar")
print()


# Items of a list

l=[1,2,3,4,5,6,7,8,9]

for items in l:
    print(items)
print()


# for loop with else

z="Muhammad Abrar"

for i in z:
    print(i)
else:
    print("finished")

print()



# Break statement

for i in range(1,21):            # for example "table of 6." 
    if i==11:
        break
    print(f"6 x {i} =",6*i)                     #Exit the loop right now.


# continue statement
for i in range(10):  # range(10) = range (0,10)
    if i==6:
        continue
    print(i)          # output---> 0 1 2 3 4 5 7 8 9 (in column)


k=(2,"abrar","khan",220,760)
for item in k:
    pass                # postpon the loop run for a while. do nothing.
                        # prevent empty block error. 
