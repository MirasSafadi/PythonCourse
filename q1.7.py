import random
L = [31,28,31,30,31,30,31,31,30,31,30,31]
m = random.randrange(12)#pick a random month
d = random.randrange(L[m])#pick a random day
sum = 0
for i in range(m):
    sum += L[i]
sum += d
print(f"{d}/{m}")
print(sum)