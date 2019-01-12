"""String Manipulation"""

phrase = "    Monty Python's Flying Circus    "

print(phrase.strip())  # 'strip' removes whitespaces from both ends
# Monty Python's Flying Circus

print(phrase.lstrip())  # 'lstrip' removes leading characters (Left-strip)
# Monty Python's Flying Circus

print(phrase.rstrip())  # 'lstrip' removes trailing characters (Right-strip)
#     Monty Python's Flying Circus
