# while True:

#     def star_pattern(n):
#         for i in range(n):
#             print("*"*(n-i))
#     n=int(input("enter a number: "))
#     star_pattern(n)

"""singe side stars pattern"""



while True:

    def star_pattern(n):
        for i in range(n+1):
            print(" "*i,end="")
            print("*"*(n-i),end=" ")
            print("*"*(n-i))
            # print("\n")
    n=int(input("enter a number: "))
    star_pattern(n)

    """double side stars pattern"""