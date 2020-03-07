import random
a = []
b = []
for i in range(12):
    a.append(random.randrange(100))
for x in a:
    if(not(x in b)):
        b.append(x)
print(a)
print(b)