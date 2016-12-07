class Rectangle():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        print("rectangle")
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getArea(self):
        return self._x*self._y
class Square(Rectangle):
    def __init__(self,x):
        self._x = x
        self._y = x
        print("square")
    def getY(self):
        print("there is no y")

class Cuboid(Rectangle):
    def __init__(self, x,y,z):
        super().__init__(x,y)
        self._z = z

    def getVolume(self):
        return self.getArea()*self._z

class Cube(Cuboid):
    def __init__(self,x):
        super().__init__(x,x,x)
