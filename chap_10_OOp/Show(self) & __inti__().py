"""Drill 6"""

class Car():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def show(self):
        print(self.brand)
        print(self.color)

audi=Car("Audi","white")
bmw=Car("BMW","Black")


audi.show()
print()
bmw.show()


"""Drill 7"""

class Student():
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def show(self):
        print(self.name)
        print(self.age)
        print(self.city)
student1=Student("Abrar",30,"Munich")
student2=Student("Ali",27,"krailing")
student3=Student("Hammad",27,"New Ulm")
student1.show()
print()
student2.show()
print()
student3.show()
print()


"""Drill 8"""

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def show(self):
        print(self.title)
        print(self.author)
        print(self.pages)
book1=Book("Naml","Humaira Ahmed",3500)
book2=Book("Passion","Abrar",10)
book1.show()
print()
book2.show()
print()