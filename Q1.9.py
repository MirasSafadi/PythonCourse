import random
class Citizen:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def __str__(self):
        return f"(name: {self.name},ID: {self.ID})"
class CityCenter:
    def __init__(self,bids = []):#bids is a list of tuples (citizen,bid)
        self.bids = bids
    def getMaxBid(self):
        lst = self.bids[:]
        lst.sort(key=lambda tup: tup[1])
        max = lst[len(lst)-1]
        del lst
        return max
    def getWinners(self):
        dic = {}
        for (citizen,bid) in self.bids:
            dic[citizen] = bid
        return dic
def main():
    bids = []
    for i in range(50):
        name = str(random.randrange(0,500))
        id = random.randrange(100000000,315891549)
        bid = random.randrange(10,10000)
        citizen = Citizen(name,id)
        bids.append((citizen,bid))
    cityCenter = CityCenter(bids)
    print(cityCenter.getMaxBid())
    print(cityCenter.getWinners())


if __name__=="__main__":main()