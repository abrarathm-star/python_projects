#     # Drill 1

# print ("Drill 1")

# class University():
#     uni="HM"
#     def __init__(self,name,Roll_no,CGPA):
#         self.name=name
#         self.Roll_no=Roll_no
#         self.CGPA=CGPA
#     @staticmethod
#     def greet():
#         print("Hello")
#     @classmethod
#     def change_uni(cls):
#         cls.uni="TUM"

#     def show(self):
#         print(self.name)
#         print(self.Roll_no)
#         print(self.CGPA)
# University.greet()
# University.change_uni()
# s1=University("Abrar",1,3.2)
# s2=University("AliK khan",2,3.5)
# s3=University("Nasir Khan",3,3.9)

# print(s1.uni)
# s1.show()
# print(s2.uni)
# s2.show()
# print(s3.uni)
# s3.show()



# Drill 2 

# print ("Drill 2")
# print()

# class MobileUser():
#     network="O2"
#     def __init__(self,phone_number):
#         self.phone_number=phone_number
#     def show(self):
#         print(self.phone_number)
#     @classmethod
#     def change_network(cls):
#         cls.network="Vodafone"
# MobileUser.change_network()
# u1=MobileUser(123)
# u2=MobileUser(456)
# u3=MobileUser(224)
# u1.show()
# print(u1.network)
# u2.show()
# print(u2.network)
# u3.show()
# print(u3.network)


# Drill 3 

# print ("Drill 3")
# print()

# class Patient():
#     hospital="klinikum TUM"
#     def __init__(self,name,age,disease):
#         self.name=name
#         self.age=age
#         self.disease=disease
#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.disease)
#     @classmethod
#     def change_hospital(cls):
#         cls.hospital="klinikum LMU"
#     @staticmethod
#     def emrgency_contact():
#         print("notruf: 123456789")
# Patient.change_hospital()
# p1=Patient("abrar", 30,"backpain")
# p2=Patient("ali",27,"fever")
# p3=Patient("Hammad",28,"headache")
# p1.show()
# print(Patient.hospital)
# print()
# p2.show()
# print(Patient.hospital)
# print()
# p3.show()
# print(Patient.hospital)
# print()


