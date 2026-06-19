# 4. Write a program to find whether a given number is prime or not.


while True:

    number=int(input("enter a number "))
    
    for i in range(2,number):
        if number%i==0:
            print("not prime number")
            break
    
    else:
        print("prime")