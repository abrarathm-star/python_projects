while True:
    name=input("Student name: ")
    physics=int(input("Physcs marks: "))
    math=int(input("math marks: "))
    chem=int(input("chemistry marks: "))
    stats=int(input("statistics marks: "))

    if physics<33:
        print("failed")
    elif math<33:
        print("failed")
    elif chem<33:
        print("failed")
    elif stats<33:
        print("failed")
    else:
        if (((physics+math+chem+stats)/400)*100)>=40:
            print("Passed")
        else:
            print("failed")