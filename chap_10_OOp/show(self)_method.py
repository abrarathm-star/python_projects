# class student():
#     def show(self):
#         print(self.name)
# abrar=student()
# abrar.name="Muhammad Abrar"
# abrar.show()


# class Material():
#     def show(object):
#         print(object.type)
# m1=Material()
# m1.type="Metal"
# m1.show()


# class Employees():
#     def show(employee):
#         print(employee.name)
# e1=Employees()
# e1.name="Nasir Khan"
# e1.show()



print("Drill 1")
class income():
    def monthly_salary(income):
        print(income.salary)
emp_class1=income()
emp_class1.salary=5000
emp_class1.monthly_salary()


class Student():
    def show(person):
        print(person.name)

s1=Student()
s1.name="Muhammad Abrar"
s1.show()
print()


print("Drill 2")
class Dog():
    def show(DOG):
        print(DOG.name,end=" ")
        print(DOG.breed)
d1=Dog()
d1.name="Tobby"
d1.breed="Roadwhiler"
d1.show()
print()


print("Drill 3")
class books():
    def show(book):
        print(book.title)
        print(book.author)
t=books()
t.title="Harry potter"
t.author="j.k Rawlings"
t.show()
print()

print("Drill 4")
class student():
    def show(self):
        print(self.name)
        print(self.age)
        print(self.city)
s1=student()
s1.name="Abrar"
s1.age=30
s1.city="Munich"
s2=student()
s2.name="Ali"
s2.age=27
s2.city="Krailing"
s1.show()
print()
s2.show()



print("Drill 5")
class employees():
    def show(self):
        print(self.name)
        print(self.position)
        print(self.salary)
employee1=employees()
employee1.name="Abrar"
employee1.position="Ai engineer"
employee1.salary=2000

employee2=employees()
employee2.name="Ali"
employee2.position="Civil engineer"
employee2.salary=3000

employee1.show()
print()
employee2.show()