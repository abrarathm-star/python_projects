def table(n):
    for i in range(1,11):
        print(f"{n} x {i} =",n*i)
while True:
    number=int(input("number: "))
    table(number)