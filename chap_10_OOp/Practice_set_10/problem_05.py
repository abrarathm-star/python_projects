class Train():
    def __init__(self,name,seat,route):
        self.name=name
        self.seat=seat
        self.route=route
    
    def show(self):
        print(self.name)
        print(self.seat)
        print(self.route)

    @staticmethod
    def num_of_seat():
        print(input("number of seats:"))
    def reserve():
        print(input("do you want to Reserve the ticket: "))
    def Header():
        print("welcome to Deutsche Bahn\nBook your tickets herr.")
    
        
train=Train("Regio",150,"Berlin via Regensberg, Bayerruth")
train.show()
Train.num_of_seat()
Train.reserve()
Train.Header( )