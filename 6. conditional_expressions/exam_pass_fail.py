while True:
    
    name=input("name: ")
    marks=int(input("enter amrks: "))
    if marks>=85 and marks<=100:
        print("4.0 CGPA")
    elif marks>=80:
        print("3.5 CGPA")
    elif marks>=75:
        print("3.0 CGPA")
    elif marks>=65:
        print("2.5 CGPA")
    elif marks>=60:
        print("2.0 CGPA")
    else:
        print("Failed")