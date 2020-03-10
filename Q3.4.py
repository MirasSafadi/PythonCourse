import random
def isPos(x):
    if x>=0:
        return True
    return False
sum = 0
for i in range(20):
    x = random.randrange(-100,100)
    if isPos(x):
        sum += x
print(sum)