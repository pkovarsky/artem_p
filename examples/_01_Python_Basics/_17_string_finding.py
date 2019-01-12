"""String Manipulation"""

phrase = "Monty Python's Flying Circus"

"""Finding"""
print(phrase.count('y'))
# 3
print(phrase.count('p'))
# 0

print(phrase.find('y'))
# 4
print(phrase.index('y'))
# 4
print(phrase.find('yy'))
# -1
print(phrase.index('yy'))
"""
Traceback (most recent call last):
  File <file>, line 23, in <module>
    print(phrase.index('yy'))
ValueError: substring not found
"""
