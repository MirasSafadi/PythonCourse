a = []
x = int(input("Enter a number (enter -1 to stop)..."))
while x != -1:
    a.append(x)
    x = int(input("Enter a number (enter -1 to stop)..."))
sum = 0
flag = False
for i in range(len(a)):
    sum += a[i]
    rest = 0
    for j in range(i+1, len(a)):
        rest += a[j]
    if sum == rest:
        flag = True
        break
    if(flag):
        break
if flag:
    print(i)
else:
    print(-1)
