# # 2-D Vector
# class Vector():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, other):
#         return (self.x+other.x),(self.y+other.y)
#     def __mul__(self, other):
#         return (self.x*other.x)+(self.y*other.y)

# vector1=[2,3]
# vector2=[4,5]
# v1=Vector(vector1[0],vector1[1])
# v2=Vector(vector2[0],vector2[1])
# print(v1+v2)
# print(v1*v2)

# # 3-D Vector
# class Vector():
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self, other):
#         return (self.x+other.x),(self.y+other.y),(self.z+other.z)
#     def __mul__(self, other):
#         return (self.x*other.x)+(self.y*other.y)+(self.z*other.z)

# v=[5,6,9]
# t=[8,3,10]
# velocity=Vector(v[0],v[1],v[2])
# time=Vector(t[0],t[1],t[2])
# print(velocity+time)
# print(velocity*time)


"""more sophisticated method"""
class Vector():
    def __init__(self,values):
        self.values=values
   
    
    def __add__(self, other):
        new_vector=[]
        for i in range(len(self.values)):
            new_vector.append(self.values[i] + other.values[i])
        return new_vector


vel=([2,3,6])
tim=([4,7,2])
velocityy=Vector(vel)
timeee=Vector(tim)
print(velocityy+timeee)