def min(x,y):
    if x<y:
        return x
    return y
x = int(input("Enter x.."))
y = int(input("Enter y.."))
w = int(input("Enter w.."))
z = int(input("Enter z.."))
print(min(min(x,y),min(w,z)))