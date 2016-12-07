class A:
    def __init__(self):
        self.X = 2
        self.Y = 3
        print("Konstruktor in A")
    def getX(self):
        return self.X
class B(A):
    def getArea(self):
        return self.X * self.Y

b = B()
print(b.getArea())
print(b.getX())
