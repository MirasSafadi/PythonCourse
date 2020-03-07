import random
a = []
for i in range(100):
    x = random.randrange(-70,101)
    a.append(x)
print(a)
#a counter list, one element for each number in the range [-70,100]
counters = [0]*171
for i in range(len(a)):
    counters[a[i]+70] += 1
print(counters)