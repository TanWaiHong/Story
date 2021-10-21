"""
探讨布尔值各种类和其用处
"""

a, b, c, = 2, 3, 10

a *= b + c
print(a)

a = 1

print(a < b)

# and 
print((a < b) and (b < c), end="\t")
print((a < b) and (a > b))

# or
print((a < b) or (b > c))

# not
print(not (a < b))
