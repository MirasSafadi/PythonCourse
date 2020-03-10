def do_something(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
l=[1,5,6,7,22,33,44,5,6]
print(do_something(l,7))
#returns True if e is in L, and False if any element in L is greater than e, and False otherwise