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
    number=Calculator(int(input("number: ")))
    Calculator.greet()
    number.show()




# class Calculator():
#     def __init__(self,square,cube,square_root):
#         self.square=square**2
#         self.cube=cube**3
#         self.square_root=square_root**(1/2)

#     def show(self):
#         print(self.square)
#         print(self.cube)
#         print(self.square_root)
# square=Calculator(int(input("number: ")))
# cube=Calculator(int(input("number: ")))
# square_root=Calculator(int(input("number: ")))
# if square==True:
#     square.show()
# elif cube==True:
#     cube.show()
# elif square_root==True:
#     square_root.show()


# class Calculator():
#     def __init__(self,number):
#         self.number=number
#     def show(self):
#         print(self.number)
# num=int(input("number: "))
# operation=input("Operation: ")
# while True:
#     if operation =="square":
#         num=Calculator((num)**2)
#         num.show()
#     elif operation=="cube":
#         num=Calculator((num))
#         num.show()
#     elif operation=="square_root":
#         num=Calculator(num**(1/2))
#         num.show