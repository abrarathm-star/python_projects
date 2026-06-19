while True:
    n=int(input("enter a number: "))
    for i in range (1,n+1):
        a="* * *"
        b="*   *"
        if i%2!=0:
            print(a)
        else:
            print(b)