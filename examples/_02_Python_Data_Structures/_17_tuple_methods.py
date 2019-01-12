"""Tuple. Methods"""

MY_TUPLE = tuple('Apple')

print(MY_TUPLE) # ('A', 'p', 'p', 'l', 'e')

print(MY_TUPLE.count('p')) # 2

print(MY_TUPLE.index('l')) # 3

print(MY_TUPLE.index('o')) 
# ValueError: tuple.index(x): x not in tuple
