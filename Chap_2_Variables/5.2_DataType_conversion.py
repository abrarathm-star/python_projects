# A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another

"""String to Integer"""

a="15"              # "15" is a string
b=int(a)            # int() is used to change a data type to integer (if possible) 
print(b)            
print(type(b))      # this we can use to check the type of variable after conversion.
print()

"""String to Float"""

c=float(a)          # flaot() is used to change a data type tp float (if possible)
print(c)
print(type(c))      # this we can use to check the type of variable after conversion.
print()

"""Integer to string"""

d=66                # 66 is an integer.
e=str(d)            # str() is used to change a data type to string (if possible)
print(e)
print(type(e))
print()             # this we can use to check the type of variable after conversion.


x="Abrar"
y=int(x)            # this is not possible (not every string can be conerted to integer)
print(y)            # it willshow Error in the output
