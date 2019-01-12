"""Regular Expressions"""

import re
phrase = "Leeloo Dallas mul-ti-pass."

result = re.findall("\w\w", phrase)
print(result)
# ['Le', 'el', 'oo', 'Da', 'll', 'as', 'mu', 'ti', 'pa', 'ss']

# Use "r" at the start of the pattern string, it designates a python raw string.
# raw strings suppress shielding
result = re.findall(r"\b\w.", phrase)
print(result)
# ['Le', 'Da', 'mu', 'ti', 'pa']
