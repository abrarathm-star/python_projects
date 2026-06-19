# Drill 06

print("Drill 06")
print()

class Student():

    school="ABC School"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        # self.school=school

    def show(self):
        print(f"name: {self.name}")
        print(f"marks: {self.marks}")
        print(f"School: {self.school}")
    def update_marks(self,updated_marks):
        self.marks+=updated_marks
    
    @staticmethod
    def welcome():
        print("welcome to the School management System")
    
    @classmethod
    def change_school(cls):
        cls.school="Oxford School"

Student.welcome()
Student.change_school()
s1=Student("Abrar",370)
print()
s1.show()
print()

s2=Student("Ali",350)
print()
s2.show()
s2.update_marks(20)
print(f"updated markes: {s2.marks}")
print()