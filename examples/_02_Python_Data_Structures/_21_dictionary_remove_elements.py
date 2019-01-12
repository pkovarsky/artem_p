"""Dictionary. Remove elements"""

MY_DICT = {'name': 'Jack', 'age': 27, 'country': 'USA', 'city':'New York'}

print(MY_DICT.pop('city'))  # New York
print(MY_DICT)  # {'name': 'Jack', 'age': 27, 'country': 'USA'}

print(MY_DICT.popitem())  # ('country', 'USA')
print(MY_DICT)  # {'name': 'Jack', 'age': 27}

del MY_DICT['age']
print(MY_DICT)  # {'name': 'Jack'}

MY_DICT.clear()
print(MY_DICT)  # {}

