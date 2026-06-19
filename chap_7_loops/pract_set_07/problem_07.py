"""
7. Write a program to print the following star pattern.
*
***
***** for n = 3    

     """
while True:
    n=int(input("enter number: "))

    for i in range(1,n+1):
        a=(" "*(n-i))
        b="*"*(2*i-1)
        print(a,end="")
        print(b,end="")
        print("\n")

