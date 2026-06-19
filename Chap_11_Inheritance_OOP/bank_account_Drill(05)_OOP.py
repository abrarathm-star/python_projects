#  Drill 5

print ("Drill 5")
print()

class BankAccont():
    bank="HBL"
    ir="15%"
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show(self):
        print(self.name)
    def deposit(self,add):
        self.balance+=add
    def withdraw(self,substrac):
        # self.balance-=substrac
        if self.balance<substrac:
            print("not enough balance")
            print(f"maximum witdraw possible {self.balance}")
        elif self.balance>0:
            self.balance-=substrac
            print(self.balance)
        else:
            pass

    @classmethod
    def change_ir(cls):
        cls.ir="12.5%"
    
customer1=BankAccont("Abrar",100)
BankAccont.change_ir()
print(customer1.bank)
customer1.show()
customer1.deposit(20)
print(customer1.balance)
print(customer1.ir)
print()


customer2=BankAccont("Ali",10)
print(customer2.bank)
customer2.show()
customer2.withdraw(20)
print(customer2.ir)