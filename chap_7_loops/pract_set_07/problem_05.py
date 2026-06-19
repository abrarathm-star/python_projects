# Write a program to find the sum of first n natural numbers using while loop.


while True:
    n=int(input("enter a number: "))
    i=1
    c=0
    while i<=n:
        c=c+i           # update the sum(value of c)
        i=i+1           # updated the running counter(value of i)
    print(c)    