from random import randrange as rr
class Traffic_Camera:
    def __init__(self,id = 0,maxSpeed = 50):
        self.id = id
        self.maxSpeed = maxSpeed
        self.speedingCars = []
    def checkCar(self,car):
        if car.speed > self.maxSpeed:
            self.speedingCars.append(car)
class Car:
    def __init__(self,speed):
        self.speed = speed
class Highway:
    def __init__(self,k):
        self.cameras = [Traffic_Camera(i,rr(50,130)) for i in range(k)]
    def speedingCars(self):
        lst = []
        for cam in self.cameras:
            lst.append(cam.speedingCars)
        return lst
    def enterCar(self,car):
        for cam in self.cameras:
            cam.checkCar(car)
def main():
    k = rr(1,25)
    street6 = Highway(k)
    for i in range(30):
        street6.enterCar(Car(rr(50,130)))
    print(street6.speedingCars())

if __name__ == "__main__": main()