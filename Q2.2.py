from math import pi
from random import randrange as rr
class Shape:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    
class Rect(Shape):
    def __init__(self, x, y, color,width,height):
        Shape.__init__(self,x, y, color)
        self.w = width
        self.h = height
    def getArea(self):
        return self.w * self.h
    def getCircumference(self):
        return 2*self.w + 2*self.h
    def display(self):
        print("Rectangle, (width,height)=(",self.w,",",self.h,") and ",self.color,"color")
class Circle(Shape):
    def __init__(self, x, y, color,radius):
        Shape.__init__(self,x, y, color)
        self.r = radius
    def getArea(self):
        return self.r**2*pi
    def getCircumference(self):
        return 2*pi*self.r
    def display(self):
        print("Circle, radius = ",self.r," and ",self.color," color")
rect1 = Rect(rr(10),rr(10),"red",rr(1,25),rr(1,25))
rect2 = Rect(rr(10),rr(10),"blue",rr(1,25),rr(1,25))
rect3 = Rect(rr(10),rr(10),"yellow",rr(1,25),rr(1,25))
circle1 = Circle(rr(10),rr(10),"red",rr(1,50))
circle2 = Circle(rr(10),rr(10),"black",rr(1,50))
shapes = [rect1,rect2,rect3,circle1,circle2]
for sh in shapes:
    sh.display()
