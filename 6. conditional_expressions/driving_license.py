# while True:
#     age=int(input("what your age: "))
#     lic=input("do you have a license: ")
#     drunk=input("are you drunk: ")

#     if age>=18 and lic=="yes" and not drunk=="yes":
#         print("ok you can go")

#     elif age>=16 and age<18 and not drunk=="yes":
#         if lic=="yes":
#             print("ok you can go" )
#         else:
#             legal_guardian=input("do you have any elder with you: ")

#             if legal_guardian=="yes" and not drunk=="yes":
#                 print("ok you can go with a sepcial permission")
            
#             else:
#                 print("you can not drive")
#     else:
#         print("you can not drive")



# + with police permission

while True:
    age=int(input("what your age: "))
    lic=input("do you have a license: ")
    drunk=input("are you drunk: ")

    if age>=18 and lic=="yes" and not drunk=="yes":
        print("ok you can go")

    elif age>=16 and age<18 and not drunk=="yes":
        if lic=="yes":
            print("ok you can go" )
        else:
            legal_guardian=input("do you have any elder with you: ")

            if legal_guardian=="yes" and not drunk=="yes":
                print("ok you can go with a sepcial permission")
            else:
                police_permission=input("do you police permission: ")
                if police_permission=="yes" and not drunk=="yes":
                    print("ok you can go wiht police permision")
                else:
                    print("you do not have permission")
            # else:
            # print("you can not drive")
    else:
        print("you can not drive")  