# range() 함수 사용
seq = range(10)
print(seq)
print(type(seq))
print(list(seq[0:]))
print(len(seq))

for i in seq:
    print(i, end=' ')
else:
    print()

seq2 = range(5, 15)
for i in seq2:
    print(i, end=' ')
else:
    print()

seq3 = range(0, -10, -1)
for i in seq3:
    print(i, end=' ')
else:
    print()

seq4 = range(0, 10, 2)
for i in seq4:
    print(i, end=' ')
else:
    print()
