# Drill 1

print ("Drill 1")
class School():
    name="ABC School"
    @classmethod
    def change_name(cls):
        cls.name="Oxford School"
School.change_name()
print(School.name)
print()



# Drill 2

print ("Drill 2")
class Laptop():
    brand="Acer"
    @classmethod
    def change_brand(cls):
        cls.brand="Asus"
l1=Laptop()
l2=Laptop()
Laptop.change_brand()
print(l1.brand)
print(l2.brand)
print()



# Drill 3

print ("Drill 3")
class Bank():
    interest_rate=5
    @classmethod
    def change_interest_rate(cls):
        cls.interest_rate=7
Bank.change_interest_rate()
ir=Bank()
print(ir.interest_rate)



# Drill 4

print ("Drill 4")

class Car():
    wheels=4
    @classmethod
    def change_wheels(cls):
        cls.wheels=6
c1=Car()
Car.change_wheels()
print(c1.wheels)