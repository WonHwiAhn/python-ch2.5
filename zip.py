# zip() 함수의 사용

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}
z = zip(seq1, seq2)

print(z, type(z))

# 순회
for t in z:
    print(t, type(t))
# 한 번 순회를 한 다음에는 또 순회가 되지 않기 때문에 현재 2번째 순회는 돌지 않음.
print('# 순회2')
for index, t in enumerate(z):
    print('{0}:{1}'.format(index, t)) # 출력결과 [(0, ('foo', 'one')), (1, ('foo', 'two'))] <= 이 형태

#unzip
# ==> zip함수를 사용하면 이런 형태로 데이터가 저장됨.
d1 = [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
# unzip ㄱㄱ
seq1, seq2 = zip(*d1)
print(seq1, type(seq1))
print(seq2)