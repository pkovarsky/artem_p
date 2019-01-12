"""Object's identity"""

A = 'str' * 2
B = 'str' * 2

print('str' * 2)  # strstr

print(A is 'str' * 2 and
      B is 'str' * 2 and
      A is B)  # True

print(id(A))         # 41573120
print(id(B))         # 41573120
print(id('str' * 2)) # 41573120

A = 'str' * 10
B = 'str' * 10

print('str' * 10)  # strstr

print(A is 'str' * 10 and
      B is 'str' * 10 and
      A is B)  # True

print(id(A))          # 40114512
print(id(B))          # 40114904
print(id('str' * 10)) # 40114960