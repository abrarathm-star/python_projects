# 1. items()
a={"key":"Value",
   
   "name":"Abrar",
   "age":"30",
   "friends":"Ashir",
   "mark_list":[45,70,84,183,55,64]}




print(a.items())                #items() returns all key-value pairs astuples.
print()



for key, Value in a.items():        # 1. loop through dictionary. each item is a touple: (key,value)
                                    # 2. we unpack it into two variables: key and vlue.
    print(key,Value)
print()



# 2. keys()

print(a.keys())     # Returns a list containing dictionary's keys.



# update()

a.update({"name":"Muhammad Abrar"})       #for multiple updates in a dictionary
print(a)
print()


# .get()

print(a.get("name"))
print()

print(a.get("mark_list"))
print()

print(a.get("friends"))

a["age"]=31                               # for a single update in a dictionary.
print(a)

a["name"]="abrar"
print(a)