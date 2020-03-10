def find(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        rest = 0
        for j in range(i+1,len(a)):
            rest += a[j]
        if sum == rest:
            return i
    return -1
L = [1,2,3,6]
print(find(L))