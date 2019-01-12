"""Regular Expressions"""

import re
phrase = "Say what again! Say what again, I dare you, I double dare you"

result = re.search("what", phrase)
print(result.group(0))
# what

result = re.search("dare", phrase)
print(result.group(0))
# dare
