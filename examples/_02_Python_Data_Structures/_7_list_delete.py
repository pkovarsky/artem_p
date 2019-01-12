"""List. Delete"""

MY_LIST = ['P', 'y', 't', 'h', 'o', 'n', ['3']]

# delete one item
del MY_LIST[2]
print(MY_LIST)  # ['P', 'y', 'h', 'o', 'n', ['3']]

del MY_LIST[2:5]  
print(MY_LIST)  # ['P', 'y', ['3']]

del MY_LIST
print(MY_LIST)
# TypeError: name 'MY_LIST' is not defined


