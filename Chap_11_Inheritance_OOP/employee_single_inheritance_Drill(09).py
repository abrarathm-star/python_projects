class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(self.name)
        print(self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def show(self):
        Employee.show(self)
        print(self.department)

p1=Manager("Abrar",20000,"R&D")
p1.show()