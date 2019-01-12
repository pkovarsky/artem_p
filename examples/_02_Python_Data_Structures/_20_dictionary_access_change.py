"""Dictionary. Access. Change"""

MY_DICT = {'lang': 'C', 1: [3]}

print(MY_DICT.get('lang'))  # C
print(MY_DICT[1])  # [3]

MY_DICT['lang'] = 'Python'
MY_DICT[True] = 'bool_key'
MY_DICT[1] = 'int_key'
MY_DICT[3.6] = 'float_key'

print(MY_DICT)  
# {'lang': 'Python', 1: 'int_key', 3.6: 'float_key'}

print(MY_DICT.get('name'))  # None
print(MY_DICT['name'])  # KeyError: 'name'



