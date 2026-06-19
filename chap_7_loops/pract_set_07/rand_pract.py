# # Q.1

# while True:
#     n=int(input("enter a number: "))

#     for i in range(1,11):
#         print(f"{n} x {i} =",n*i)

# Q.2 

# # while True:
# l=["abrar", "ashir", "ahmed",
#        "musab","mutthaharr","asghar",
#        "anees","shakir", "sikander"]
# for i in l:
#         if i.startswith("a"):
#             print("Good morning",i)
# else:
#     print("good morning")


# Q.3

# while True:
#     m=int(input("enter a number: "))
#     i=1
#     while i<11:
#         print(f"{m} x {i} =",m*i)
#         i=i+1

# Q.4

# while True:
#     h=int(input("enter a number: "))
#     if h%2==0:
#         print("prime number")
#     else:
#         print("not prime")

# Q.5

# # while method
# while True:
#     j=int(input("enter a number: ")) 
#     i=1
#     a=0
#     while i<=j:
#         a=a+i
#         i=i+1
#     print(a)


# loop metod

# while True:
#     k=int(input("enter a number: "))
#     a=0
#     b=1
#     for i in range(k):
#         a=a+b
#         b=b+1
#     print(a)


# Q.6

# while True:
#     l=int(input("enter anumber "))
#     c=1
#     for i in range(1,l+1):
#         c=c*i
#     print(c)

# Q.7

# while True:
#         n=int(input("enter a number: "))
#         for i in range(n+1):
#                 print(" "*(n-i),end="")
#                 print("*"*(2*i-1),end="")
#                 print("\n")
                

# Q.8
# while True:
#     number=int(input("enter a number: "))
#     for i in range(number+1):
#         print("*"*(2*i-1))

# Q.9

while True:
    num=int(input("enter a number: "))
    a="* * *"
    b="*   *"
    for i in range(num+1):
        if i%2==0:
            print(a)
        else:
            print(b)