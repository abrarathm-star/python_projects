while True:

    def sum_natural_number(n):
        if n==0:
            return 0
        else:
            return n+sum_natural_number(n-1)
    n=int(input("enter a number: "))
    print(sum_natural_number(n))