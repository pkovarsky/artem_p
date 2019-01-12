"""Regular Expressions"""

import re
phrase = "Leeloo Dallas mul-ti-pass."

result = re.findall("\w*", phrase)
print(result)
# ['Leeloo', '', 'Dallas', '', 'mul', '', 'ti', '', 'pass', '', '']

''' Again, it is returning space as a word because "*" 
returns zero or more matches of pattern to its left. 
Now to remove spaces we will go with "+".
'''

result = re.findall("\w+", phrase)
print(result)
# ['Leeloo', 'Dallas', 'mul', 'ti', 'pass']
