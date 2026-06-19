while True:
    def c_to_f(t):
        Temp_in_f=(9/5)*c+32
        return Temp_in_f
    c=float(input("Temp in celsuius: "))
    print(c_to_f(c))