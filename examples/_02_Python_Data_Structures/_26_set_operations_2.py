"""SET"""

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# True if empty intersection
print(A.isdisjoint(B))  # False

# True if A set is subset of B set
print(A.issubset(B))  # True

# True if B set contains A set
print(B.issuperset(A))  # True

# Remove all elements of A set from B set
B.difference_update(A)
print(B)  # {4, 5}

