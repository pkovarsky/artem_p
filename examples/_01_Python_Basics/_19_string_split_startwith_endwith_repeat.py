"""String Manipulation"""

phrase = "Monty Python's Flying Circus"

"""Split"""
print(phrase.split(' ')) # Split on whitespace
# ['Monty', "Python's", 'Flying', 'Circus']

"""Startswith / Endswith"""
print(phrase.startswith("Python"))
# False
print(phrase.startswith("M"))
# True
print(phrase.endswith("Circus"))
# True
print(phrase.endswith("s"))
# True


"""Repeat Strings"""
print("." * 10)
# ..........
print(phrase * 3)
# Monty Python's Flying CircusMonty Python's Flying CircusMonty Python's Flying Circus