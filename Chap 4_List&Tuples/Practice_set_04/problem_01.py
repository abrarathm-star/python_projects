# a=input("fruit 1 ")
# b=input("fruit 2 ")
# c=input("fruit 3 ")
# d=input("fruit 4 ")
# e=input("fruit 5 ")
# f=input("fruit 6 ")
# g=input("fruit 7 ")
# fruits=[a,b,c,d,e,f,g]
# print(fruits)                       

# """this is correct but beginnerslevel"""
fruits=[]
for i in range(7):
    a=input(f"fruit {i+1}: ")
    fruits.append(a)        # we can put the entire value of a in append(a) i.e append(input(f"fruit {i+1}: ")n)
print()
print(fruits)     