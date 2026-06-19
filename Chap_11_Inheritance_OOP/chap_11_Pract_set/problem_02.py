class Animal():
    def __init__(self):
        pass
class Pet(Animal):
    def __init__(self):
        pass
class Dog(Pet):
    def __init__(self):
        super().__init__()
    @staticmethod
    def bark():
        print("the dog Barks")
a1=Dog()
a1.bark()