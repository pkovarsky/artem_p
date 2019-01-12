

"""List. Built-in Functions"""

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 8, 7]

print(all(NUMBERS))     # False
print(any(NUMBERS))     # True
print(len(NUMBERS))     # 9
print(max(NUMBERS))     # 8
print(min(NUMBERS))     # 0
print(sum(NUMBERS))     # 36
print(sorted(NUMBERS))  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(NUMBERS)          # [0, 1, 2, 3, 4, 5, 6, 8, 7]

NUMBERS = [0, '1', [2]]

print(all(NUMBERS))  # False
print(any(NUMBERS))  # True
print(len(NUMBERS))  # 3
print(max(NUMBERS))  # TypeError: '>' not supported between instances of 'str' and 'int'
print(min(NUMBERS))  # TypeError: '<' not supported between instances of 'str' and 'int'
print(sum(NUMBERS))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(list(enumerate(NUMBERS)))  # [(0, 0), (1, '1'), (2, [2])]

