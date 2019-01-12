"""Regular Expressions"""

import re
phrase = "Say what again! Say what again, I dare you, I double dare you"
pattern = re.compile("Say")

result = pattern.findall(phrase)
print(result)
# ['Say', 'Say']

# string manipulations
result = re.sub("what", "regex", phrase)
result = re.sub("dare", "endorse", result)

result = pattern.findall(result)
print(result)
# ['Say', 'Say']
