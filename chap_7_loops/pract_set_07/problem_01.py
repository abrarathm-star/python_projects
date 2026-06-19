# 1. Write a program to print multiplication table of a given number using for loop.

given_number=int(input("enter number: "))
for i in range(1,11):
    print(f"{given_number} x {i} =",given_number*i)