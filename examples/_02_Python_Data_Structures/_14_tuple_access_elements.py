"""Tuple"""

MY_TUPLE = ('P', 'y', 't', 'h', 'o', 'n', ['3'])

print(MY_TUPLE[0])  # P
print(MY_TUPLE[2])  # t
print(MY_TUPLE[4])  # o
print(MY_TUPLE[-1][0])  # 3
print(MY_TUPLE[4.0]) 
"""
Traceback (most recent call last):
  File <file>, <line>, in <module>
    print(MY_TUPLE[4.0])  # o
TypeError: tuple indices must be integers or slices, not float
"""

