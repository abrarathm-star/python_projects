while True:
    def sum_factorial(n):
        if n==1:
            return 1
        else:
            return n+sum_factorial(n-1)
    num=int(input("number: "))
    print(sum_factorial(num))