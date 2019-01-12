"""Mutable and Immutable"""

# Dictionary is mutable object
STUDENTS = ["Jules Winnfield"]

STUDENTS.append("Vincent Vega")

print(STUDENTS)  # ['Jules Winnfield', 'Vincent Vega']

# String is immutable object
NAME = "Masha"

NAME[0] = "S"
# TypeError: 'str' object does not support item assignment