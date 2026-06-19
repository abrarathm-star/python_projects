# Drill 1

print("Drill 1")
class Student():
    university="HM"
    @classmethod
    def chnage_uni(cls):
        cls.university="TUM"
Student.chnage_uni()
print(Student.university)
print()


# Drill 2

print("Drill 2")
class Car():
    wheels=4

    @classmethod
    def change_wheels(cls):
        cls.wheels=6
    
Car.change_wheels()
print(Car.wheels)
print()


# Drill 3

print("Drill 3")
class Employee():
    company="Google"
    @classmethod
    def change_company(cls):
        cls.company="Microsoft"
e1=Employee()
e2=Employee()
Employee.change_company()
print(e1.company)
print(e2.company)
print()


# Dril 4

print("Drill 4")
class Students():
    uni="Hochule Muenchen"
    def show(self):
        print(self.university)
s1=Students()
s1.university="TUM"
s1.show()
print(s1.uni)
print()
