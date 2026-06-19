# Dictionary is a collection of keys-value pairs.

a={"key":"Value",
   
   "name":"Abrar",
   "age":"30",
   "friends":"Ashir",
   "mark_list":[45,70,84,183,55,64]}

print(type(a))      # output ---> <class 'dict'>
print()

print(a["name"])    # output ---> Abrar
print()

print(a["mark_list"])   # output ---> [45, 70, 84, 183, 55, 64]
print()



#  Dictionaries ---> Mutable:

a["name"]="Muhammad Abrar"
print()
print(a)

a["mark_list"]=[45,70,84,183,55,64,78,69]
print()
print(a)
print()



# print(a[0])                                         # we can not use index value to call an object in a dictionary.

print(a["friends"])      # output ---> Ashir          # we can use "key" value to call an object in a dictionary

# PROPERTIES OF PYTHON DICTIONARIES

""" 1. It is unordered.

    2. It is mutable.

    3.It is indexed.

    4. Cannot contain duplicate keys."""