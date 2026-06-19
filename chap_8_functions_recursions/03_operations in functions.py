# # addition funtion

# def add(a,b):
#     c=a+b
#     return c
# x=add(2,3)
# print(x)          # function call


# greeting function

# def greet(name):
#     greeting="Hello "+name
#     return greeting
# a=greet("Nasir")
# print(a)          # function call


# Even/Odd function
# while True:
#     def even_odd(number):
#         if number%2==0:
#             return "even"
#         else:
#             return"odd"
#     number=int(input("enter a number "))
#     print(even_odd(number))           # function call


# largest number function
# while True:
#     def largest_number(a,b):
#         if a>b:
#             return a
#         elif b>a:
#             return b
#         else:
#             return "equal"
#     a=int(input("enter number a: "))
#     b=int(input("enter number b: "))
#     print(largest_number(a,b))            # function call


# positive_negaive function
# while True:
#     def positive_negtive(num):
#         if num>0:
#             return "positive"
#         elif num<0:
#             return "negative"
#         elif num==0:
#             return "0"
#         else:
#             return "not integer"
#     num=float(input("enter a number: "))
#     print(positive_negtive(num))               # function call


# -ve ---> +ve conversion

# while True:
#     def negative_to_positive(number):
#         if number<0:
#             return number*(-1)
#         else:
#             return number
#     a=float(input("enter a number: "))
#     print(negative_to_positive(a))             # function call


# celsius to fahrenheit

# while True:
#     def C_to_F(temp):
#         T=(9/5)*(temp)+32
#         return T
#     temp=int(input("enter a number: "))
#     print(C_to_F(temp))                         # function call


# Square function

# while True:
#     def square(a):
#         sqr=a**2
#         return sqr
#     num=int(input("enter a number: "))
#     print(square(num))                           # function call


# cube function

# while True:
#     def cube(number):
#         c_e=number**3
#         return c_e
#     num=int(input("enter a number: "))
#     print(cube(num))                             # function call


# greeting function

# while True:
#     def greet(name):
#         greeting="Hello "+name
#         return greeting
#     name=input("name: ")
#     print(greet(name))            # function call


# area of rectangle

# while True:
#     def area_of_rectangle(length,width):
#         area=length*width
#         return area
#     length=int(input("enter length: "))
#     width=int(input("enter width: "))
#     print(area_of_rectangle(length,width))            # function call


# is_adult

while True:
    
    def is_adult(age):
        if age>=18:
            return "Adult"
        elif age<18 and age>=1:
            return "Minor"
        else:
            return "wrong age"
    age=int(input("age: "))
    print(is_adult(age))                                   # function call    


