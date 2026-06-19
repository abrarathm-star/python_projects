# # """This is important"""

# # Without super()

# class Employee():                       # Parent's Class
#     def __init__(self):     # constructor
#         print("employee constructor")

# class Programmer(Employee):             # child class
#     def __init__(self):     # constructor
#         print("programmer constructor")
# p=Programmer()
# print(p)

# # output ---> programmer constructor
# """when Python finds a constructor in the child class, it runs that one and ignores the parent's constructor"""



# with super()

class Employee():                       # Parent's Class
    def __init__(self):     # constructor
        print("employee constructor")

class Programmer(Employee):             # child class
    def __init__(self):     # constructor
        super().__init__()
        print("programmer constructor")
p=Programmer()
print(p)

# output ---> employee constructor 
#             programmer constructor



# Rules
""" 1. if child class has its own constructor then the parents class constructor 
        is ignored untill super() is applied.
        
    2.  if child class has no constructor then python automatically uses the parents
        class constructor."""
# e.g.

class Employee():                       # Parent's Class
    def __init__(self):     # constructor
        print("employee constructor")

class Programmer(Employee):             # child class   
    pass
p=Programmer()
print(p)