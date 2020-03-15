import random
class triangle:
    def __init__(self,x,y,z):
        if not (x+y>z or x+z>y or y+z>x):
            raise Exception("not a triangle!")
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
def main():
    trs = []
    i=0
    while i < 3:
        (x,y,z) = (random.randrange(1,25),random.randrange(1,25),random.randrange(1,25))
        try:
            trs.append(triangle(x,y,z))
            i+=1
        except:
            print("not a triangle")
    for tr in trs:
        print(tr)
if __name__ == "__main__": main()