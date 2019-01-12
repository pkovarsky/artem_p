"""List. Change"""

ODD = [2, 4, 6, 8]

ODD[0] = 1    
print(id(ODD))  # 48804448

ODD[1:4] = [3, 5, 7] 
print(id(ODD))  # 48804448
print(ODD)  # [1, 3, 5, 7]

EVEN = [2, 4, 6, 8]
print(id(EVEN))  # 46510688 

EVEN += [10]
print(id(EVEN))  # 46510688
print(EVEN)  # [2, 4, 6, 8, 10]

EVEN = EVEN + [12]
print(id(EVEN))  # 46510888: Even now is a new object.
print(EVEN)  # [2, 4, 6, 8, 10, 12]

