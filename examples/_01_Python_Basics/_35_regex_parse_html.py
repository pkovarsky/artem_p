"""Regular Expressions"""

import re
html = """
<div class="user">
 <span class="firstname">Leeloo</span>
 <span class="lastname">Dallas</span>
</div>
<div class="user">
 <span class="firstname">Korben</span>
 <span class="lastname">Dallas</span>
</div>
<div class="user">
 <span class="firstname">Ruby</span>
 <span class="lastname">Rhod</span>
</div>
"""

result = re.findall(r'<span \w+="\w+">(\w+)</span>', html)
print(result)
# ['Leeloo', 'Dallas', 'Korben', 'Dallas', 'Ruby', 'Rhod']
