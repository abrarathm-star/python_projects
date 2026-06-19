class Dog():
    def __init__(self,name,color):
        self.name=name
        self.color=color
tommy = Dog("Tommy","black")
print(tommy.name)


class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
python_book=Book("python Handbook","Harry")
print(python_book.author)


class Mobile():
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
mobile_phone=Mobile("iphone",500000)
print(mobile_phone.brand)


class Student():
    def __init__(self,name,age,university):
        self.name=name
        self.age=age
        self.university=university
nasir=Student("Nasir",35,"Dow university")
print(nasir.university)



