
class ComplexNumber():
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value
    def __mul__(self, other):
        return self.value*other.value
    def __truediv__(self, other):
        return  self.value/other.value

c1=complex(1,2)
c2=complex(3,4)
cn1=ComplexNumber(c1)
cn2=ComplexNumber(c2)

print(cn1+cn2)

print(cn1*cn2)

print(cn1/cn2)