#with single elements
# Existence check
print(2 in {1, 2, 3})
#True
print(4 in {1, 2, 3})
#False
print(4 not in {1, 2, 3})
#True
# Add and Remove
s = {1,2,3}
print(s)
s.add(4)
print(s)
s.discard(3)
print(s)
s.discard(5) # does not throw exception
print(s)
s.remove(2)
print(s)
# s.remove(2)
# print(s)