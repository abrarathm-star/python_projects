# class Animal():
#     def __init__(self,name,age,breed,color,weight):
#         self.name=name
#         self.age=age
#         self.breed=breed
#         self.color=color
#         self.weiht=weight
#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.breed)
#         print(self.color)
#         print(self.weiht)


# class Dog(Animal):
#     def __init__(self, name, age, breed, color, weight,role):
#         self.role=role
#         super().__init__(name, age, breed, color, weight)
#     def dangerous(self):
#         if self.breed=="german shephard":
#             print("it can be dangerous")
#         else:
#             pass    
#     def show(self):
#         Animal.show(self)
#         print(self.role)


# class Puppy(Dog):
#     def __init__(self, name, age, breed, color, weight,role,teeth):
#         super().__init__(name, age, breed, color, weight,role)
#         self.teeth=teeth
    
#     def play(self):
#         if self.age>0 and self.age<2:
#             print("playful")
#         else:
#             pass
#     def show(self):
#         Dog.show(self)
#         print(self.teeth)

# p1=Puppy("kiku",1.5,"german shephard","white",3.5,"hunter",12)
# p1.play()
# p1.show()
# p1.dangerous()






class Animal():
    def __init__(self,name,age,breed,color,weight):
        self.name=name
        self.age=age
        self.breed=breed
        self.color=color
        self.weiht=weight
    def show(self):
        print(self.name)
        print(self.age)
        print(self.breed)
        print(self.color)
        print(self.weiht)


class Dog(Animal):
    def __init__(self, name, age, breed, color, weight,role):
        self.role=role
        super().__init__(name, age, breed, color, weight)
    def dangerous(self):
        if self.breed=="german shephard":
            print("it can be dangerous")
        else:
            pass    
    def show(self):
        super().show()
        print(self.role)


class Puppy(Dog):
    def __init__(self, name, age, breed, color, weight,role,teeth):
        super().__init__(name, age, breed, color, weight,role)
        self.teeth=teeth
    
    def play(self):
        if self.age>0 and self.age<2:
            print("playful")
        else:
            pass
    def show(self):
        super().show()
        print(self.teeth)

p1=Puppy("kiku",1.5,"german shephard","white",3.5,"hunter",12)
p1.play()
p1.show()
p1.dangerous()