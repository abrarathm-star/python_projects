# while True:
#     age=int(input("age: "))
#     has_id=input("do you have ID: ")
#     if age>=16 and has_id=="yes":
#         print("allowed")
#     else:
#         print("not allowed")



# use "or"

# while True:
#     age=int(input("enter age: "))
#     parents_permis=input("parents mission: ")
#     if age>=18 or parents_permis=="yes":
#         print("allowed")
#     else:
#         print("not allowed")



# use of "not"

# while True:
    
#     age=int(input("enter age: "))
#     banned=input("are you banned: ")
#     parents_permis=input("parents mission: ")
#     print()

#     if age>=18 and not banned=="yes":
#         print("allowed")
#     elif parents_permis=="yes":
#         print("allowed")
#     else:
#         print("not allowed")
#         print()




while True:
    
    age=int(input("enter age: "))
    parents_permis=input("parents mission: ")
    banned=input("are you banned: ")
    print()

    if age>=18 and not banned=="yes":
        print("allowed")
    elif parents_permis=="yes" and not banned=="yes" :
        print("allowed")
    else:
        print("not allowed")
        print()