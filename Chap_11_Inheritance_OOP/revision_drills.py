# Drill 1

class Student():
    university="HM Munich"
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
    @classmethod
    def change_uni(cls):
        cls.university="Hochschule Muenchen"
s1=Student("Abrar")
s1.show()
Student.change_uni()
print(s1.university)


# Drill 2

class Calculator():
    pass
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
        
print(Calculator.is_even(3423445344524))



#  Drill 3

class Temperature():
    def __init__(self,temp):
        self._temp=temp
    @property
    def temp_in_farenheit(self):
        return (9/5)*self._temp+32
t1=Temperature(40)
print(t1.temp_in_farenheit)


#  Drill 4

class bankAccount():
    def __init__(self,balance):
        self._balance=balance
    @property
    def new_balance(self):          
        return self._balance           # @property and .setter should be defined with the same function
    @new_balance.setter                    # i.e. def balance() should be for both
    def new_balance(self,amount):
        if amount>0:
            self._balance=self._balance+amount
        else:
            print("Invalid amount")
c1=bankAccount(3000)
c1.new_balance=2000
print(f"your account balance is: {c1.new_balance}")



#  Drill 5

class Employee():
    def __init__(self,salary):
        self.salary=salary
    def __add__(self, other):
        return self.salary+other.salary
e1=Employee(2000)
e2=Employee(2500)
print(e1+e2)


#  Drill 6

class Person():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return (f"Good morning {self.name}")
p1=Person("Abrar")
print(p1)



# Drill 7
class Driver():
    def __init__(self,working_hours):
        self.working_hours=working_hours
    def __len__(self):
        return self.working_hours
d1=Driver(10)
print(len(d1))