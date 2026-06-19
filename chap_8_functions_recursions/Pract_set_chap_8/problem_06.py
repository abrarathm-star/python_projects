while True:
    def inches_cm(inch):
        centimeters=(inch*2.54)
        return centimeters
    inch_value=float(input("inches: "))
    print(inches_cm(inch_value),end=" ")
    print("cm")