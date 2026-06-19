#  Drill 4

print ("Drill 4")
print()

class Player():
    max_health=100
    gameversion=1.0
    def __init__(self,name,):
        self.name=name
        self.current_health=100
    def show(self):
        print(self.name)
    def take_dmage(self,damge):
        self.current_health=self.current_health-damge
    @staticmethod
    def opening():
        print("welcome to the game")
    @classmethod
    def change_version(cls):
        cls.gameversion=2.0
Player.change_version()
pl1=Player("abrar")
print(pl1.max_health)
pl1.show()
pl1.take_dmage(20)
print(pl1.current_health)
print(pl1.gameversion)
print()
pl2=Player("ali")
print(pl2.max_health)
pl2.show()
pl2.take_dmage(40)
print(pl2.current_health)
print(pl2.gameversion)
print()