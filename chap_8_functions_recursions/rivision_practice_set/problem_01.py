while True:

    def greatest_number(a,b,c):
        if a>b and a>c:
            print("a")
            return a
        elif b>a and b>c:
            print("b")
            return b
        elif c>a and c>b:
            print("c")
            return c
    
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    c=int(input("enter c: "))
    print(greatest_number(a,b,c))