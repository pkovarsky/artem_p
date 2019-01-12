"""Tuple. Change"""

NUMBERS = ([1], 2, 4, 6, 8)

NUMBERS[0][0] = 0
print(NUMBERS)  # ([0], 2, 4, 6, 8)

NUMBERS[0] = 1
# TypeError: 'tuple' object does not support item assignment    

NUMBERS[1:4] = (3, 5, 7)
# TypeError: 'tuple' object does not support item assignment    

del NUMBERS[0]
# TypeError: 'tuple' object doesn't support item deletion


