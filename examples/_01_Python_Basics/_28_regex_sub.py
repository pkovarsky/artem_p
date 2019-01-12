"""Regular Expressions"""

import re
phrase = "Say what again! Say what again, I dare you, I double dare you"

result = re.sub("what", "regex", phrase)
print(result)
# Say regex again! Say regex again, I dare you, I double dare you

result = re.sub("dare", "endorse", result)
print(result)
# Say regex again! Say regex again, I endorse you, I double endorse you
