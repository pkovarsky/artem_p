"""Regular Expressions"""

import re
phrase = "Before would've been better but... before is over."

result = re.match("better", phrase)
print(result)  # None


result = re.match("Before", phrase)
print(result)  # <_sre.SRE_Match object at 0x7f226ffb56b0>

"""Above, it shows that pattern match has been found. 
To print the matching string we'll use method group 
(It helps to return the matching string)."""

print(result.group(0))  # Before

print('Start: %s, End: %s' % (result.start(), result.end()))
# Start: 0, End: 6
