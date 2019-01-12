"""List. Methods"""

CHARS = list("Monty Python")
print(CHARS)
# ['M', 'o', 'n', 't', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n']

print(CHARS.index('o'))  # 1
print(CHARS.count('o'))  # 2

CHARS.sort()
print(CHARS)
# [' ', 'M', 'P', 'h', 'n', 'n', 'o', 'o', 't', 't', 'y', 'y']

CHARS.reverse()
print(CHARS)
# ['y', 'y', 't', 't', 'o', 'o', 'n', 'n', 'h', 'P', 'M', ' ']