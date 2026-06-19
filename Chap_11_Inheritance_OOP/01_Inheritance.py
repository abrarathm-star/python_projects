"""Inheritance is a way of creating a new class from an existing class."""


# 1. Single Inheritance

# class Employee():
#     company="Google"

#     def show(self):
#         print("I am an Ai Engineer")
# class ai_engineer(Employee):
#     pass
# p=ai_engineer()
# print(p.company)
# p.show()



#  2. Multiple Inheritance

# class Camera():
#     def click(self):
#         print("take a photo")

# class phone():
#     def phone(self):
#         print("calling...")
# class smart_phone(Camera,phone):
#     pass

# sp=smart_phone()
# sp.click()
# sp.phone()


#  3. Multilevel Inheritance

class Animal():
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class Puppy(Dog):
    pass
pup=Puppy()
pup.eat()
pup.bark()

"""Tree"""

#   Animal
#      |
#     Dog
#      |
#     Puppy
"""Puppy inherited from Dog and Dog inherited from Animal so Puppy gets eaverything"""