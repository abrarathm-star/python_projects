# # class Student():
# #     def __init__(self,marks):
# #         self._marks=marks
    
# #     @property
# #     def marks(self):
# #         return self._marks+5
# # s1=Student(90)
# # print(s1.marks)
# # print()



# # class BankAccount():
# #     def __init__(self,balance):
# #         self._balance=balance

# #     @property                         # Getter (only read variable)
# #     def balance(self):
# #         return self._balance 
# #     @balance.setter                   # @setter (edit variable)
# #     def balance(self,deposit):
# #         if deposit>0:
# #             self._balance=deposit
# #         else:
# #             print("not valid amount")
# # c1=BankAccount(20000)
# # c1.balance=22000
# # print(c1.balance)
# # print()



# # class EmployeeName():
# #     def __init__(self,name):
# #         self._name=name
    
# #     @property
# #     def name(self):
# #         return self._name.upper()
# # e1=EmployeeName("AbRar")
# # print(e1.name)
# # print()



# # class Temperature_converter():
# #     def __init__(self,temp_celsius):
# #         # self._temp_farenheit=(9/5)*temp_farenheit+32
# #         self._temp_celsius=temp_celsius
# #     @property
# #     def temp_farenheit(self):
# #         return self._temp_celsius*(9/5)+32
    
# # t1=Temperature_converter(38)
# # temp_in_farenheit=t1.temp_farenheit
# # print(temp_in_farenheit)
# # print()


# class Employee():
#     def __init__(self,salary):
#         self._salary=salary
    
#     @property
#     def salary(self):
#         pass
    
#     @salary.setter
#     def salary(self,amount):
#         if amount>0:
#             self._salary=amount
#         else:
#             print("invalid salary")
# e1=Employee(2800)
# e1.salary=-1
# print(e1.salary)