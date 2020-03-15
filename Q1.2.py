import random
class Part:
    partNumber = 0
    prices = {
        "agriculture":9,
        "building":23,
        "industry": 40
    }
    def __init__(self,area = 100,target = "agriculture"):
        self.partNo = Part.partNumber
        Part.partNumber += 1
        self.area = area
        self.target = target
    def getTarget(self):
        return self.target
    def getPrice(self):
        return Part.prices[self.target]*self.area
    def __str__(self):
        return f"Part No. {self.partNo} is estimated at {self.getPrice()}"
def computePrices(parts):
    agricultureSum = 0
    buildingSum = 0
    industrySum = 0
    for part in parts:
        if(part.getTarget() == "agriculture"):
            agricultureSum += part.getPrice()
        elif(part.getTarget() == "building"):
            buildingSum += part.getPrice()
        else:
            industrySum += part.getPrice()
        return (agricultureSum,buildingSum,industrySum)
def main():
    targets = {"agriculture", "building", "industry"}
    partList = [Part(random.randrange(100,10000),random.sample(targets,1)[0]) for i in range(7)]
    for part in partList:
        print(part)
    print("total price for (agriculture,building,industry)")
    print(computePrices(partList))
if __name__ == "__main__": main()