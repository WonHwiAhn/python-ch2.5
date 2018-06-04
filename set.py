# set 생성

s = {1, 2, 3, 3}
print(s, type(s))

# 기본연산
print(len(s))
print(2 in s)
print(2 not in s)

# list의 중복되는 항목을 제거할 때 유용
print('# list의 중복되는 항목을 제거할 때 유용')
nums = [1, 2, 3, 2, 2, 4, 5, 5, 6]
s = set(nums)
print(s)

nums2 = list(s)
print(nums2)

# 객체함수(메서드)
s.add(7)
print(s)

# 요소 제거
s.discard(2)
print(s)

# 요소 제거
s.remove(3)
print(s)

# add랑 비슷(결과적으로는 add와 같음)
# add는 {}형태로 추가가 안됨.
s.update({2, 3, 4})
print(s)

# 요소 모두 삭제
s.clear()
print(s)

# 수학 집합 관련 객체 함수
print('# 수학 집합 관련 객체 함수')
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

# 합집합
s3 = s1.union(s2)
print(s3)

# 교집합
s4 = s1.intersection(s2)
print(s4)

# 차집합
s5 = s1.difference(s2)
print(s5)

# 대칭차집합
s6 = s1.symmetric_difference(s2)
print(s6)

# 부분집합인지 묻는 여부
# s1은 s4의 부분집합이냐
print(s1.issuperset(s4))
print(s5.issuperset(s1))