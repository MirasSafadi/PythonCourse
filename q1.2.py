import random
L = []
x = random.randrange(100)
for i in range(x):
    if(i < int(x/2)):
        L.append(0)
    else:
        L.append(1)
print(L)
