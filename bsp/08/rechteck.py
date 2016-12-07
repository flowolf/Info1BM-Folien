
class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getArea(self):
        return self.y*self.x

class Square(Rectangle):
    def __init__(self,x):
        self.x = x
        self.y = x

class Cuboid(Rectangle):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    def getVolume(self):
        return self.getArea()*self.z

class Cube(Cuboid):
    def __init__(self,x):
        super().__init__(x,x)
        self.z = x
