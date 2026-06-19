# 6. Write a program to calculate the factorial of a given number using for loop.


while True:
    n=int(input("enter a number: "))
    b=1
    for i in range (1,(n+1)):
        b=b*i
    print(b)