import random
class Box:
    def __init__(self,h=1.0,w=1.0,l=1.0):
        self.h = h
        self.w = w
        self.l = l
    def __str__(self):
        return f"box height: {self.h}\nbox width: {self.w}\nbox length: {self.l}"
    def getVolume(self):
        return self.h*self.w*self.l
def main():
    boxes = ()
    
    for i in range(10):
        (h,w,l) = (random.randrange(1,10),random.randrange(1,10),random.randrange(1,10))
        boxes += ((h,w,l),)
    lst = []
    for (x,y,z) in boxes:
        lst.append(Box(x,y,z))
    del boxes
    sumVols = 0
    for box in lst:
        sumVols += box.getVolume()
        print(box)
        print("--------------")
    print("total volumes: ",sumVols)
    
if __name__ == "__main__": main()