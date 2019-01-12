"""List. Methods"""

NUMBER = [1, 2, 3]

NUMBER.append(4)
print(NUMBER)  # [1, 2, 3, 4]

NUMBER.append([4])
print(NUMBER)  # [1, 2, 3, 4, [4]]

NUMBER.extend([4])
print(NUMBER)  # [1, 2, 3, 4, [4], 4]

NUMBER.extend('42')
print(NUMBER)  # [1, 2, 3, 4, [4], 4, '4', '2']

NUMBER.extend(4)
# TypeError: 'int' object is not iterable

