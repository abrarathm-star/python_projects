# while True:
#     def stars(n):
#         for i in range(n):
#             if n==1:
#                 return "*"*1
#             else:
#                 return "*"*(n-i)
#     n=int(input("enter a number:"))
#     print(stars(n))

while True:
    def stars(n):
        for i in range(0,n):
            print("*"*(n-i))
    
    n=int(input("enter a number:"))
    print(stars(n))