from random import randrange as rr
from random import choice
class Flight:
    def __init__(self,dest = 1,price = 10 ,maxSeats = 50,passengers = [],flightNo = 1):
        self.dest = dest
        self.price = price
        self.maxSeats = maxSeats
        self.passengers = passengers
        self.flightNo = flightNo
    def isFull(self):
        return len(self.passengers) == self.maxSeats
    def addCustomer(self,customer):
        self.passengers.append(customer)
    def removeCustomer(self,customer):
        self.passengers.remove(customer)

class Customer:

    def __init__(self,ID = 0,lastName = "Hope",firstName = "Bob",address = "California",phone = "555-678"):
        self.ID = ID
        self.lastName = lastName
        self.firstName = firstName
        self.address = address
        self.phone = phone

class ShalomTours:
    def __init__(self,k = 1,flights = []):
        self.waitingList = [[]*k] # a 2D list of Customers
        self.flights = flights # a list of Flights
    def buyTicket(self,dest,customer):
        if not self.flights[dest].isFull:
            self.waitingList[dest].append(customer)
            print("No more seats left, you're in the waiting list!")
        else:
            self.flights[dest].addCustomer(customer)
            print("congrats!")
    def cancelTicket(self,dest,customer):
        if not customer in self.flights[dest].passengers:
            print("You are not a passenger on this flight")
        else:
            self.flights[dest].removeCustomer(customer)
            cust = self.waitingList[dest][0]
            self.waitingList[dest].pop(0)
            self.flights[dest].addCustomer(cust)
def main():
    k = random.randrange(100)
    flights = []
    for i in range(k):
        flights.append(Flight(i,rr(10,500),rr(50,100),flightNo=i))
    shalom = ShalomTours(k,flights)
    #create 500 customers
    customers = []
    for i in range(500):
        customers.append(Customer(i))
    # do whatever you want...

if __name__ == "__main__":main()