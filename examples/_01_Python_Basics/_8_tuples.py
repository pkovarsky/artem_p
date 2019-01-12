"""Tuples"""
# Generally tuples are used for heterogeneous (different) datatypes.

empty_tuple = ()
print(empty_tuple)  # ()

integers_tuple = (1, 2, 3)
print(integers_tuple)  # (1, 2, 3)

mixed_tuple = (1, "Hello World", 3.14)
print(mixed_tuple)  # (1, 'Hello World', 3.14)

nested_tuple = ("cat", [4, 5, 0], (7, 3, 1))
print(nested_tuple)
# ('cat', [4, 5, 0], (7, 3, 1))

tuple_without_parentheses = 3.14, 8.5, "monkey"
print(tuple_without_parentheses)
# (3.14, 8.5, 'monkey')

a, b, c = tuple_without_parentheses

print(a)  # 3.14
print(b)  # 8.5
print(c)  # monkey
