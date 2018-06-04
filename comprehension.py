# list comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = []

for num in nums:
    result = num ** 2
    results.append(result)

print(results)

results = [ num * num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0]
print(results)

# 문자열 리스트에서 길이가 2 이하인 문자열 리스트 만들기
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = [s for s in strings if len(s) < 2]

print(strings)

# 1~100 사이의 수중에 짝수 리스트 만들기
print('1~100 사이의 수중에 짝수 리스트 만들기')
evens = [i for i in range(1, 101) if i % 2 == 0]
print(evens)

# set comprehension
print('# set comprehension')
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = {s for s in strings if len(s) <= 2}
print(strings)

# 문자열 리스트에서 문자열 길이를 set으로 저장해보자
print('# 문자열 리스트에서 문자열 길이를 set으로 저장해보자')
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = {len(s) for s in strings}
print(lens, type(lens))

# dict comprehension
print('# dict comprehension')
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
dicts = {s:len(s) for s in strings}
print(dicts, type(dicts))

# values = {i for i in range(1,100)}
print({i for i in range(1, 100) if i // pow(10, (len(str(i)))-1) % 3 == 0 and len(str(i)) > 1})
print({i for i in range(1, 100) if i % 10 % 3 == 0 and i % 10 != 0})