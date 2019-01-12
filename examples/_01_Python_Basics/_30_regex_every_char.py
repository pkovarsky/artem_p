"""Regular Expressions"""

import re
phrase = "Leeloo Dallas mul-ti-pass."

result = re.findall(".", phrase)
print(result)
# ['L', 'e', 'e', 'l', 'o', 'o', ' ', 'D', 'a', 'l', 'l', 'a', 's', ' ',
# 'm', 'u', 'l', '-', 't', 'i', '-', 'p', 'a', 's', 's', '.']

result = re.findall("\.", phrase)
print(result)
# ['.']

# alphanumeric only
result = re.findall("\w", phrase)
print(result)
# ['L', 'e', 'e', 'l', 'o', 'o', 'D', 'a', 'l', 'l', 'a', 's',
# 'm', 'u', 'l', 't', 'i', 'p', 'a', 's', 's']
