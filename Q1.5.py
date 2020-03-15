from math import pi
class Circle:
    def __init__(self,x=0,y=0,r=1):
        self.x = x
        self.y = y
        self.r = r
    def __str__(self):
        return f"Circle is centered at ({self.x},{self.y}) with radius {self.r}"
    def expand(self,alpha):
        self.r *= alpha
    def move(self,newX,newY):
        self.x = newX
        self.y = newY
    def getPerimeter(self):
        return 2*pi*self.r
    def getArea(self):
        return pi**2*self.r
def main():
    c1 = Circle(3,2,4)
    c2 = Circle(5,3,2)
    print("area of first circle ",c1.getArea)
    print("perimeter of second circle ",c2.getPerimeter)
    del c2
    c1.expand(2)
    print(c1)
    c1.move(4,2)
    print(c1)
    print("area:")
    print(c1.getArea())
    print("perimeter:")
    print(c1.getPerimeter())
if __name__ == "__main__": main()