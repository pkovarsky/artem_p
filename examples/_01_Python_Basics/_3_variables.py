"""Variables and Types"""

# Variables need no declaration
a = 1

# Objects always have a type
print(type(a))
# <type 'int'>

a = 'Hello'
print(type(a))
# <type 'str'>

print(type(1.0))
# <type 'float'>

# Variables must be created before they can be used
b
"""
Traceback (most recent call last):
  File "<file>", line 20, in <module>
    b
NameError: name 'b' is not defined
"""
