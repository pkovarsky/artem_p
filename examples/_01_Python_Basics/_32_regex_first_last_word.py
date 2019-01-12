"""Regular Expressions"""

import re
phrase = "Leeloo Dallas mul-ti-pass."

result = re.findall("^\w+", phrase)
print(result)
# ['Leeloo']

result = re.findall("(\w+)\.$", phrase)
print(result)
# ['pass']
