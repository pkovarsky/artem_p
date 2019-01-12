"""Dictionaries"""

favorites = {}

# Any immutable object can be a dictionary key
favorites['number'] = 3

favorites[3] = 'Python'

favorites[True] = 3

print(favorites)
# {True: 3, 3: 'Python', 'number': 3}

print(len(favorites))
# 3
