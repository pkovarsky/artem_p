"""Regular Expressions"""

import re
phrase = "Say what again! Say what again, I dare you, I double dare you"

result = re.split("what", phrase)
print(result)
# ['Say ', ' again! Say ', ' again, I dare you, I double dare you']

maxsplit = 1
result = re.split("what", phrase, maxsplit)
print(result)
# ['Say ', ' again! Say what again, I dare you, I double dare you']
