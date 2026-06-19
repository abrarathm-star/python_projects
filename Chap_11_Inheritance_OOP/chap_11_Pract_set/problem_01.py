class Vector_2D():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"x = {self.x}")
        print(f"y = {self.y}")
class Vector_3D(Vector_2D):
    def __init__(self, x, y,z):
        super().__init__(x,y)
        self.z=z
    
    def show(self):
        super().show()
        print(f"z = {self.z}")

# v_2d=Vector_2D(2,3)
v_3d=Vector_3D(2,3,4)
v_3d.show()