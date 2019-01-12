"""String Manipulation"""

phrase = "I won't be back!"

"""Replace"""
phrase = phrase.replace("I won't", "I'll")  # 'replace' returns new string
print(phrase)
# I'll be back!

"""Join"""
phrase = ' '.join(phrase)  # 'join' returns new string
print(phrase)
# I ' l l   b e   b a c k !

"""Reverse"""

# 'reversed' returns an iterator, which you can make into a string using the join method
print(''.join(reversed(phrase)))
# ! k c a b   e b   l l ' I

print(phrase[::-1])
# ! k c a b   e b   l l ' I
