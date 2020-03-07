import random
# L = [[0,1,0,0,1,0,0,0],
#     [1,0,0,0,0,0,1,0],
#     [0,0,1,0,0,1,0,0],
#     [0,1,0,0,0,0,1,0],
#     [0,0,2,1,0,0,1,0],
#     [0,1,0,0,0,0,1,0]]
n = 6
m = 8
L = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        L[i][j] = random.randrange(0,2)
print(L)
for i in range(n):
    sum = 0
    for j in range(m):
        sum += L[i][j]
        # if(L[i][j] == 0 or L[i][j] == 1):
        #     sum += L[i][j]
        # else:
        #     print("error")
        #     break
    if(sum%2 != 0):
        print("error")
        break
print(L)
