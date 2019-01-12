"""Mutable and Immutable"""

# String is immutable object
NAME = "Masha"

print(id(NAME))    # 34952512
print(id("Masha")) # 34952512

"""
In this example NAME variable get new reference.
And refers to new object, string "Pasha"
But value of the string object "Masha" is not changed
"""

NAME = "Pasha"

print(id(NAME))    # 34952448
print(id("Pasha")) # 34952448