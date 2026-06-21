# Q.1 
class Vector_2D():
    def __init__(self,values):
        self.values=values
class Vector_3D(Vector_2D):
    def __init__(self,values,z):
        super().__init__(values)
        self.z=z
    def __add__(self, other):
        added_vector=[]
        for i in range(len(self.values)):
            added_vector.append(self.values[i]+other.values[i])
        added_vector.append(self.z+other.z)
        return added_vector
    


v2xy=([9,5])
vector_3D1=Vector_3D(v2xy,2)
vector_3D2=Vector_3D(v2xy,2.035)
print(vector_3D1+vector_3D2)



#  Q.4

# class Vector():
#     def __init__(self,value):
#         self.value=value
    
#     def __str__(self):
#         for i in range(len(self.value)):
#             return f"{self.value[0]}i + {self.value[1]}j + {self.value[2]}k"
# v=([7,8,10])
# vector=Vector(v)
# print(vector)




# Q.5

# class Vector():
#     def __init__(self,values):
#         self.values=values
    
#     def __add__(self, other):
#         vector=[]
#         for i in range(len(self.values)):
#             vector.append(self.values[i]+other.values[i])
#         return vector
    
#     def __mul__(self, other):
#         dot_pro=0
#         for i in range(len(self.values)):
#             # self.values[i]*other.values[i]
#             dot_pro=dot_pro+(int(self.values[i])*int(other.values[i]))
#         return dot_pro
# v1=([2,4,5])
# v2=([6,3,9])
# vector1=Vector(v1)
# vector2=Vector(v2)
# print(vector1+vector2)
# print(vector1*vector2)


