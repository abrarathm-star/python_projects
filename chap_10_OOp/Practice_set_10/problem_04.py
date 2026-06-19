class Calculator():
    def __init__(self,num):
        self.num=num
    @staticmethod
    def greet():
        print("Hello")
    def show(self):
        print((self.num)**2)
        print((self.num)**3)
        print((self.num)**(1/2))

while True:
    Calculator.greet()
    number=Calculator(int(input("Number: ")))

# num=int(input("Number: "))
    number.show()