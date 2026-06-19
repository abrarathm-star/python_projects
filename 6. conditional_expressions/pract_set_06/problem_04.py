while True:
    user_name=input("user name: ")
    if len(user_name)<10:
        print("allowed")
        # user_name=True
    else:
        print("not allowed")