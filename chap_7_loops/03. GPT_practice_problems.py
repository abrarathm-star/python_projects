# # numbers 1-50 (while loop)

# a=1
# while a<51:
#     print(a)
#     a=a+1
# print()


# # numbers 50 - 1 (while loop)

# b=50
# while b<51 and b>=1:
#     print(b)
#     b=b-1
# print()


# # numbers 1-50 (for loop)

# for i in range(51):
#     print(i)
# print()



# # numbers 50 - 1 (for loop)

# for k in range (50,0,-1):
#     print(k)
# print()



# # table of a number with user input
# number=int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{number} x {i} =",number*i)



# # number from 1 - 30 skipping 15

# for c in range(1,31):           # using for loop
#     if c==15:
#         continue        # only for for loops.
#     print(c)


#             #using while loop
# f=1                             # stating value
# while f<31:                     # loop runs from 1-30
#     if f==15:                   # python check if f=15
#         f=f+1                   # python makes f=15 to f=16 by adding +1
#         continue                # then continue
#     print(f)                    # print numbers except 15
#     f=f+1                       # increase the value of f by +1.


#  number 1 - 100, break at 25.

for t in range(1,101):
    if t==25:
        break
    print(t)