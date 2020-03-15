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
class Block:
    def __init__(self,parts = []):
        self.parts = parts
    def area(self):
        sum = 0
        for part in self.parts:
            sum += part.area
        return sum
    def getTargetArea(self, tar):
        sum = 0
        for part in self.parts:
            if part.target == tar:
                sum += part.area
        return sum
    def getPartArea(self,partID):
        for part in self.parts:
            if part.partNo == partID:
                return part.area
        return -1
    def getPartTarget(self,partID):
        for part in self.parts:
            if part.partNo == partID:
                return part.target
        return ""
    def getPartPrice(self,partID):
        for part in self.parts:
            if part.partNo == partID:
                return part.getPrice()
        return -1
    def addPart(self,part):
        self.parts.append(part)
    def __getIndex(self,partID):
        for i in range(len(self.parts)):
            if self.parts[i].partNo == partID:
                return i
        return -1
    def removePart(self,partID):
        i = self.__getIndex(partID)
        if i != -1:
            parts.pop(i)
def main():
    targets = ["agriculture", "building", "industry"]
    prices = [9,23,40]
    partList = [Part(random.randrange(100,10000),random.choice(targets)) for i in range(7)]
    b1 = Block(partList)
    sum = 0
    for i in range(3):
        price = b1.getTargetArea(targets[i])*prices[i]
        sum += price
    print("total block price is: $",sum)
    partList = [Part(random.randrange(100,10000),random.choice(targets)) for i in range(7)]
    b2 = Block(partList)
    print("total industry parts area: $",b2.getTargetArea(targets[2]))
    
if __name__ == "__main__": main()