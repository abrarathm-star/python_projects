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
        vector=[]
        for i in range(len(self.values)):
            vector.append(self.values[i]+other.values[i])
        return vector
    
    def __mul__(self, other):
        dot_pro=0
        for i in range(len(self.values)):
            # self.values[i]*other.values[i]
            dot_pro=dot_pro+(int(self.values[i])*int(other.values[i]))
        return dot_pro
v1=([2,4,5])
v2=([6,3,9])
vector1=Vector(v1)
vector2=Vector(v2)
print(vector1+vector2)
print(vector1*vector2)