def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
l = [77, 2, 4, 99, 1, 88, 9, 2]
print(l)
bubble_sort(l)
print(l)
#sorts L