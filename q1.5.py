import random
a = []
sum = 0
for i in range(20):
    x = random.randrange(-10,31)
    a.append(x)
    sum += x
if(sum == 210):#the sum of natural number from 1 to 20: s = (20/2)*(2*1+(20-1)*1) = 210
    print("all numbers from 1..20 are there")
else:
    print("boo!")