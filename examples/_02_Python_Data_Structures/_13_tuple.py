"""Tuples"""

'''Creating a tuple with one element is a bit tricky.
Having one element within parentheses is not enough. 
We will need a trailing comma to indicate that it is in fact a tuple.
'''
# only parentheses is not enough
MY_TUPLE = ("Python")
print(type(MY_TUPLE))  # <class 'str'>

# need a comma at the end
MY_TUPLE = ("Python",)
print(type(MY_TUPLE))  # <class 'tuple'>

# parentheses is optional
MY_TUPLE = "Python",
print(type(MY_TUPLE))  # <class 'tuple'>