"""Dictionary. Methods"""

MY_DICT = {'name': 'Jack', 'age': 27, 'country': 'USA', 'city':'New York'}

print(MY_DICT.items()) 
# dict_items([('name', 'Jack'), ('age', 27), ('country', 'USA'), ('city', 'New York')])
print(MY_DICT.keys())  
# dict_keys(['name', 'age', 'country', 'city'])
print(MY_DICT.values()) 
# dict_values(['Jack', 27, 'USA', 'New York'])

MY_DICT_2 = dict.fromkeys(['age', 'weight'], 45)  #{'age': 45, 'weight': 45}
MY_DICT_2.setdefault('lastname', 'Harper')

MY_DICT.update(MY_DICT_2)
print(MY_DICT) 
# {'name': 'Jack', 'age': 45, 'country': 'USA', 
# 'city': 'New York', 'weight': 45, 'lastname': 'Harper'}


