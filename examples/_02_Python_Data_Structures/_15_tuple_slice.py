"""Tuple. Slice"""

MY_TUPLE = ('P', 'y', 't', 'h', 'o', 'n', ['3'])

# elements from second to 6th
print(MY_TUPLE[1:6])  # ('y', 't', 'h', 'o', 'n')

# elements without last one
print(MY_TUPLE[:-1])  # ('P', 'y', 't', 'h', 'o', 'n')

# elements from 6th to end
print(MY_TUPLE[6:])  # [['3']]

# elements from begining to end (copy of the list)
print(MY_TUPLE[:])  # ('P', 'y', 't', 'h', 'o', 'n', ['3'])

# elements from end to begining ( reversed copy of the list)
print(MY_TUPLE[::-1])  # (['3'], 'n', 'o', 'h', 't', 'y', 'P')

# elements from 6th to begining ( reversed )
print(MY_TUPLE[5::-1])  # ('n', 'o', 'h', 't', 'y', 'P')

