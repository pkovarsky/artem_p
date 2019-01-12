"""Regular Expressions"""

import re
phrase = "Say what again! Say what again, I dare you, I double dare you"

result = re.findall("what", phrase)
print(result)
# ['what', 'what']

result = re.findall("double", phrase)
print(result)
# ['double']

result = re.findall("triple", phrase)
print(result)
# []
