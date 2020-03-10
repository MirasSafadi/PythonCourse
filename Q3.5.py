def do_some_thing(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
l = [18, 5, 68, 7, 22, 33, 44, 5, 6]
print(do_some_thing(l, 7))
#returs True if e is in L, otherwise False
