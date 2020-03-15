class Range:
    # assume a<=b
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dist(self):
        return self.b-self.a

    def shift(self, y):
        self.a += y
        self.b += y

    def mid(self):
        return (self.b-self.a)/2

    def __str__(self):
        return f"[{self.a},{self.b}]"


def main():
    print("hi")
    r1 = Range(-1, 0)
    r2 = Range(-3, -2)
    r3 = Range(0, 12)
    r4 = Range(5, 8)
    r5 = Range(12, 18)
    L = [r1, r2, r3, r4, r5]
    sum = 0
    for r in L:
        sum += r.dist()
    print("total distances: ", sum)
    print("r1 is: ", r1)
    print("shifting r1 by 2")
    r1.shift(2)
    print("r1 is now: ", r1)
    print("shifting r1 by -2")
    r1.shift(-2)
    print("r1 is now: ", r1)


if __name__ == "__main__": main()