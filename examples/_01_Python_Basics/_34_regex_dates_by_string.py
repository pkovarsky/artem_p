"""Regular Expressions"""

import re
phrase = "foo 65-3546 08-06-1987, baz 321-4782 16-01-2012, bat 61117-8445 01-01-1977"

result = re.findall("\d{2}-\d{2}-\d{4}", phrase)
print(result)
# ['08-06-1987', '16-01-2012', '01-01-1977']


result = re.findall("\s(\d{2,5}-\d{4})", phrase)
print(result)
# ['08-06-1987', '16-01-2012', '01-01-1977']

result = re.findall("[A-Za-z]+", phrase)
print(result)
# ['08-06-1987', '16-01-2012', '01-01-1977']