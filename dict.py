# 사전 생성
print('# 사전 생성')
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

print('# 인덱싱 대신 키로 접근해야 한다.')
print(d['basketball'])

# 연결(+) 지원하지 않는다.
# print(d + {'valleyball': 6})

d['valleyball'] = 6
print(d)

# 반복(*) 지원하지 않는다.
# print(d * 2)

print('#len() ------')
print(len(d))

print('soccer' in d)
print('valleyball' in d)

print('다양한 dict 생성 방법 -----------')
# empty dict, d = {}도 가능하다
d = dict()  # dict()함수를 사용하는 방법
print(type(d))

d = {}  # empty dict (literal을 사용하는 방법)
print(type(d))

# dict() 함수 사용
# keyword argument를 사용하는 방법
d = dict(one=1, two=2)
print(d)

# dict() 함수 사용
# tuple list를 사용하는 방법
d = dict([('one', 1), ('two', 2)])
print(d)

# dict() 함수를 사용하는 방법
# zip객체를 사용하는 방법
keys = ('one', 'two', 'three')
value = (1, 2, 3)
print(zip(keys, value)) # 순회할 때 사용가능
print(dict(zip(keys, value)))

print('다양한 dict의 key 타입')
d = {}  # 반 dict 생성
print(d)

d[True] = 'true'
d[10] = '10'

d['twenty'] = 20
d[(1, 2, 3)] = '6'

"""
# 튜플을 넣어논 것을 생각해보면
t = (1, 2, 3)   # t라는 튜플을 생성해준다.
d[t] = '6'  # t튜플을 키로 가지고 있는 dict의 값을 6으로 생성
t[0] = 10   # t[0]을 10으로 변경하려면 키값이 변화하기 때문에 에러가 된다. (키값은 바뀌면 안됨.)
"""

"""
# 오류: list는 mutable이기 때문에 key값으로 사용할 수 없다
# d[[1, 2, 3]] = '6'
# keynums = [1, 2, 3]
# d[keynums] = '6'
# keynums[0] = 10
"""

print(d)

print('# keys() 객체함수==========')
keys = d.keys()
print(keys)
print(type(keys))

for key in keys:
    print('{0}:{1}'.format(key, d[key]))

print('# values() 객체함수 --------')
values = d.values()
print(values)
print(type(values))

for value in values:
    print('{0}'.format(value))

print('# items() 객체함수 --------')
items = d.items()
print(items)

# phone자체를 변수에 넣으면 서로 완벽히 같은 값이 된다.
print('# copy() 객체함수 ---------')
phone = {'둘리': '0000-0000-0000',
         '도우넛': '1111-1111-1111',
         '또치': '2222-2222-2222'}
p = phone
print(phone)
print(p)
# 값을 phone에만 추가했지만 p를 추가했을 때도 값이 추가되어있음
phone['마이콜'] = '3333-3333-3333'
print(phone)
print(p)


phone = {'둘리': '0000-0000-0000',
         '도우넛': '1111-1111-1111',
         '또치': '2222-2222-2222'}
p = phone.copy()
print(phone)
print(p)

print('# get() 객체함수 ---------')

print(phone['둘리'])
print(phone.get('둘리'))

# 이 둘의 차이는 없는 값을 지목했을 때 차이가 있다.
# get함수를 이용하면 없는 값을 지목해도 에러가 나지 않고 None값이 들어가게 된다.
name = phone.get('길동')
print(name)
# name = phone['길동']

name = phone.get('길동', '0000-0000-0000')
print(name)

# cf : 차이점은 실제로 사전에 저장된다.
print(phone)
# setdefault를 사용하게 되면 값이 추가된다.
print('# setdefault')
print(phone.setdefault('길동', '0000-0000-0000'))
print(phone)

# 삭제와 동시에 값 가져오기.
print('# 삭제와 동시에 값 가져오기.')
name = phone.pop('둘리')
print(name) # 값이 들어가 있음.
print(phone)

# 튜플로 가져오기
print('# 튜플로 가져오기')
item = phone.popitem()
print(item)
print(phone)

print('# update(), clear() 객체함수 ------------')
phone.update({'도우넛': '010-1111-1111',
              '또치': '010-2222-2222'})
print(phone)

phone.clear()
print(phone)

print('dict 조회 -----------')
d = {'c': 3, 'a': 1, 'b': 2}

for key in d:
    print(key, end=' ')
else:
    print('')

for key in d.keys():
    print(key + ":" + str(d[key]), end=' ')
else:
    print('')

for key, value in d.items():
    print(key + ":" + str(value), end=' ')
    print('{0}:{1}'.format(key, value), end=' ')
else:
    print('')