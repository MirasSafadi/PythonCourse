# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})
# {3,4,5}
# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6})
print({1, 2, 3, 4, 5} | {3, 4, 5, 6})
# {1,2,3,4,5,6}
# Difference
{1, 2, 3, 4}.difference({2, 3, 5})
print({1, 2, 3, 4} - {2, 3, 5})
# {1,4}
# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5})
print({1, 2, 3, 4} ^ {2, 3, 5})
# {1,4,5}
# Superset check
{1, 2}.issuperset({1, 2, 3})
print({1, 2} >= {1, 2, 3})
# False
# Subset check
{1, 2}.issubset({1, 2, 3})
print({1, 2} <= {1, 2, 3})
# True
# Disjoint check
print({1, 2}.isdisjoint({3, 4}))
# True
print({1, 2}.isdisjoint({1, 4}))
# False