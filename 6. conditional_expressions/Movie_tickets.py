# while True:

#     age=int(input("enter age: "))
#     # parents_per=input("do you have parents permission: ")
#     banned=input("are you banned: ")

#     if age>=16 and not banned=="yes":
#         print("allowed")
    
#         # parents_per=input("do you have parents permission: ")
#     elif age<16 and not banned=="yes":
#             parents_per=input("do you have parents permission: ")
#             print("allowed")
#     elif parents_per=="yes" and not banned=="yes":
#             print("allowed")
#     else:
#         print("not allowed")


# while True:

#     age=int(input("enter age: "))
#     # parents_per=input("do you have parents permission: ")
#     banned=input("are you banned: ")

#     if age>=16 and not banned=="yes":
#         print("allowed")
    
#         # parents_per=input("do you have parents permission: ")
#         if age<16 and not banned=="yes":
#             parents_per=input("do you have parents permission: ")
#             print("allowed")
#         elif parents_per=="yes"and not banned=="yes":
#     elif not banned=="yes":
#           print("allowed")
#     else:
#         print("not allowed")


while True:

    age=int(input("enter age: "))
    banned=input("are you banned: ")

    if age>=16 and not banned=="yes":
        print("allowed")

    elif age<16 and not banned=="yes":
        parents_per=input("do you have parents permission: ")
        if parents_per=="yes" and not banned=="yes":        # nested if
            print("allowed")
        else:
            print("not allowed")
    else:
        print("not allowed")

    """this is perfect code for movie tickets system"""