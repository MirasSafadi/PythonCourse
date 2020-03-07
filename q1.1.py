import random
L = []
sum = 0
for i in range(10):
    x = random.randrange(100)+1
    sum += x
    L.append(x)
avg = sum/10
print(L)
for x in L:
    print("distance from avg:")
    print(round(abs(x-avg),1))