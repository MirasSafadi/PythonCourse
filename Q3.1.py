# def f(y):
#     x = 1
#     x += 1
#     print(x)

# x = 5
# f(x)
# print(x)
#prints 2 and then 5
#----------------------------------------------
print("----------------------------------------")
def f(y):
    global x
    x += 1
    print(x)
x = 5
f(x)
print(x)
