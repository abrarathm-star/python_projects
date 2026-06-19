# Drill 07

print("Drill 07")
print()

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Teacher(Person):
    def __init__(self,name,age,subject):
        self.subject=subject
        super().__init__(name,age)
    def show(self):
        print(self.name)
        print(self.age)
        print(self.subject)

class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def show(self):
        print(self.name)
        print(self.age)
        print(self.marks)


t1=Teacher("Abrar",30,"Physics")
t1.show()
print()
s1=Student("khan",31,390)
s1.show()