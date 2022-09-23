a = True
b = False
print(a and b)
print((a and b) or b)
print((a and b) or not (a and b))
print(a and b or not (a or b) or b)
print(b and b or not a and (a or b or a) or not (a or b))
print(1 << 2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111 ^ 0b111 | 0b010)
