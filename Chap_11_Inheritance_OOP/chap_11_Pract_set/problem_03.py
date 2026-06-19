# class Employee():
#     def __init__(self,salary):
#         self._salary=salary

#     @property
#     def salary_after_incremnet(self):
#         return self._salary
    
#     @salary_after_incremnet.setter
#     def salary_after_incremnet(self):
#         if self._salary >1500 and self._salary<2000:
#             self._salary+(self.self._salary*0.1)
#         elif self._salary > 200:
#             self._salary+(self._salary*0.11)
#         elif self._salary<1500:
#             self._salary+(self._salary*0.15)
# e1=Employee(2100)
# e1.salary_after_incremnet=2100
# print(e1.salary_after_incremnet)


# class Employee():
#     def __init__(self,salary):
#         self._salary=salary

#     @property
#     def salary_after_incremnet(self):
#         return self._salary
    
#     @salary_after_incremnet.setter
#     def salary_after_incremnet(self,curent_salary):
#         if curent_salary >1500 and curent_salary<2000:
#             self._salary=self._salary+(self._salary*0.1)
#         elif curent_salary > 2000:
#             self._salary=self._salary+(self._salary*0.11)
#         elif curent_salary<1500:
#             self._salary=self._salary+(self._salary*0.15)
# e1=Employee(2100)
# e1.salary_after_incremnet=2100
# print(e1.salary_after_incremnet)


class Employee():
    def __init__(self,salary,increment):
        self._salary=salary
        self.increment=increment

    @property
    def salary_after_incremnet(self):
        return self._salary
    
    @salary_after_incremnet.setter
    def salary_after_incremnet(self,curent_salary):
        if curent_salary >1500 and curent_salary<2000:
            self._salary=self._salary+(self._salary*0.1)
        elif curent_salary > 2000:
            self._salary=self._salary+(self._salary*0.11)
        elif curent_salary<1500:
            self._salary=self._salary+(self._salary*0.15)
e1=Employee(2100)
e1.salary_after_incremnet=2100
print(e1.salary_after_incremnet)