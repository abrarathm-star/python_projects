# Q.7 If the names of 2 friends are same; what will happen to the program in problem 6?


d={}

for i in range(4):
    friend=input(f"name {i+1}: ")
    favourite_language= input(f"language {i+1}: ")
    d[friend]=favourite_language

print(d)

""" 1. dictionary does not keep the duplicate keys.
    2. latest key replaces the old one."""



# Q.8 If languages of two friends are same; what will happen to the program in problem 6?

"""Same values(languages) are alowed in dictionaries as long as the friend(key) is different"""