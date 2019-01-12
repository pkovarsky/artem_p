"""String Manipulation"""

phrase = "Monty Python's Flying Circus"

"""Slicing
Use [ # : # ] to get set of letter
Keep in mind that python, as many other languages, starts to count from 0!! 
"""

print(phrase[0])    # get one char of the word
# M
print(phrase[0:1])  # get one char of the word (same as above)
# M
print(phrase[0:6])  # get the first six chars
# Monty
print(phrase[:6])   # get the first six chars
# Monty
print(phrase[-6:])  # get the last six chars
# Circus
print(phrase[6:])   # get all but the six first chars
# Python's Flying Circus
print(phrase[:-6])  # get all but the three last character
# Monty Python's Flying
print(phrase[6:15] + phrase[-6:])
# Python's Circus
