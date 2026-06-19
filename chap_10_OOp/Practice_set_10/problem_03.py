# class Car():
#     color="Black"
#     def __init__(self,brand):
#         self.brand=brand
#         # self.color=color
#     def show(self):
#         print(self.brand)
#         print(self.color)
# car1=Car("BMW")
# car1.show()

class Car():
    color="a"
    def __init__(self,brand):
        self.brand=brand
    def show(self):
        print(self.brand)
        print(self.color)
car1=Car("BMW")
# car1.color="yellow"
# Car.color="Pink"
Car.color=0
car1.show()

