while True:
    age=int(input("age: "))
    member=input("are you a member: ")
    amount=int(input("purchase amount: "))
    student=input("are you a student: ")
    banned=input("are you banned: ")

    if (age<=25 or member=="yes" or student=="yes") and not banned=="yes" and amount>=30:
        print("30% Off")

    elif age>25 and age<35:
        if not banned=="yes" and amount>=50:
            print("30% OFF")
        else:
            ex_millitary=input("are you a vateran: ")
            if ex_millitary=="yes" and amount==25:
                print("30% OFF")
            else:
                police=input("are you in Police: ")
                if police=="yes" and amount==25:
                    print("20% OFF")
                else:
                    Teacher=input("are you a teacher: ")
                    if Teacher=="yes" and amount==25:
                        print("20% OFF")
                    else:
                        print("5% OFF")

    else:
        print("0% OFF   ")
    print()

"""this one is better"""

# while True:
#     age=int(input("age: "))
#     member=input("are you a member: ")
#     amount=int(input("purchase amount: "))
#     student=input("are you a student: ")
#     banned=input("are you banned: ")

#     if (age<=25 or member=="yes" or student=="yes") and not banned=="yes" and amount>=30:
#         print("30% Off")

#     elif (age>=18 and not banned=="yes"):
#         if amount>=50:
#             print("30% OFF")
#         else:
#             print("0% OFF")
#     elif (age >=18 and amount>=25 or member=="yes")and not banned=="yes":
#         ex_millitary=input("are you a vateran: ")
#         if ex_millitary=="yes":
#             print("30% OFF")
#         else:
#             print("0% OFF")
#     elif (age >=18 and amount>=25 or member=="yes")and not banned=="yes":
#         police=input("are you in Police: ")
#         if police=="yes":
#             print("20% OFF")
#         else:
#             print("0% ")
#     elif (age >=18 and amount>=25 or member=="yes")and not banned=="yes":
#         Teacher=input("are you a teacher: ")
#         if Teacher=="yes":
#             print("20% OFF")
#         else:
#             print("0% OFF")
#     else:
#         print("0% OFF")
#     print()     