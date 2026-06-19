class Employee():
    def __init__(self,salary):
        self.salary=salary
    def __add__(self, other):
        return self.salary+other.salary

e1=Employee(2000)
e2=Employee(2100)
print(e1+e2)


    
class Worker():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return (f"Hello Goodmorning {self.name}")
w1=Worker("Abrar")
print(w1)


class Driver():
    def __init__(self,working_hours):
        self.working_hours=working_hours
    def __len__(self):
        return self.working_hours
d1=Driver(10)
print(len(d1))