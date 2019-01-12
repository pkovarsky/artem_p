"""SET"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print(A | B) # print(A.union(B))
# {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
print(A & B) # print(A.intersection(B))
# {4, 5}

# Difference
print(A - B, B - A) # print(A.difference(B), B.difference(A))
# {1, 2, 3} {8, 6, 7}

# Symmetric Difference
print(A ^ B) # print(A.symmetric_difference(B))
# {1, 2, 3, 6, 7, 8}

