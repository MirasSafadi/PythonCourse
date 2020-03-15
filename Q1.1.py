class Song:
    def __init__(self, name="some name", artist="some artist", duration=0):
        self.name = name
        self.artist = artist
        self.duration = duration
    
    def getName(self):
        return self.name
    def getArtist(self):
        return self.artist
    def getDuration(self):
        return self.duration
    def __str__(self):
        return f"{self.name}, by {self.artist} {self.duration} minutes"


class Book:
    def __init__(self, name = "Some book", author = "Alex", pages = 10, price = 2):
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price

    def getName(self):
        return self.name
    def getAuthor(self):
        return self.author
    def getPages(self):
        return self.pages
    def getPrice(self):
        return self.price
    def __str__(self):
        return f"{self.name}, written by {self.author}, {self.pages} pages long just for ${self.price}"


class Lesson:
    def __init__(self, subject = "Linear Algebra", lecturer = "Mark", duration = 2):
        self.subject = subject
        self.lecturer = lecturer
        self.duration = duration

    def getSubject(self):
        return self.subject
    def getLecturer(self):
        return self.lecturer
    def getDuration(self):
        return self.duration
    def __str__(self):
        return f"{self.subject}, lectured by {self.lecturer}, duration {self.duration}"

class BankAccount:
    def __init__(self, accountNumber = 123456, accountHolder = "Alice", balance = 0):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = balance

    def getAccountNumber(self):
        return self.accountNumber
    def getAccountHolder(self):
        return self.accountHolder
    def getBalance(self):
        return self.balance
    def __str__(self):
        return f"Account number {self.accountNumber}, held by {self.accountHolder} has balance {self.balance}"

def main():
    song1 = Song("Love me tender","Elvis Presley",90)
    song2 = Song("Love me tender","Elvis Presley")
    song3 = Song("Love me tender")
    print(song1,"\n",song2,"\n",song3)
    print("artist")
    print(song1.getArtist())
    print(Song.getArtist(song1))
    print("---------------------------------------------")
    book1 = Book("The guilty wife","Robert Frost",180,10)
    book2 = Book("The guilty wife","Robert Frost",180)
    book3 = Book("The guilty wife","Robert Frost")
    book4 = Book("The guilty wife")
    print(book1,"\n",book2,"\n",book3,"\n",book4)
    print("---------------------------------------------")
    lesson1 = Lesson("Calculus 101","Aviv Tsinzur",2)
    lesson2 = Lesson("Calculus 101","Aviv Tsinzur")
    lesson3 = Lesson("Calculus 101")
    print(lesson1,"\n",lesson2,"\n",lesson3)
    print("---------------------------------------------")
    bankAccount1 = BankAccount(415164,"Miras Safadi",800)
    bankAccount2 = BankAccount(415164,"Miras Safadi")
    bankAccount3 = BankAccount(415164)
    print(bankAccount1,"\n",bankAccount2,"\n",bankAccount3)
    print("---------------------------------------------")

if __name__ == "__main__": main()