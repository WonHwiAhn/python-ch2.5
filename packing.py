# packing은 tuple로만 가능

t = 10, 20, 30, 'python'

print(t)
print(type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# 변수가 값보다 더 적을 경우 (too many values to unpack error)
# a, b, c = t
# print(a, b, c)

# 변수가 값보다 더 많을 경우 (not enough values to unpack error)
# a, b, c, d, e = t
# print(a, b, c)

# unpacking extended
t = (1, 2, 3, 4, 5)
a, *b = t
print(a)
print(b)

*a, b = t
print(a)
print(b)

a, b, *c = t
print(a)
print(b)
print(c)

a, *b, c = t
print(a)
print(b)
print(c)