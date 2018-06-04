# enumerate() 함수 사용

i = 0
for color in ['red', 'yellow', 'blue', 'black', 'gray']:
    print('{0}:{1}'.format(i, color))
    i += 1

# cf: using enumerate()
print('# cf: using enumerate()')
for index, color in enumerate(['red', 'yellow', 'blue', 'black', 'gray']):
    print('{0}:{1}'.format(index, color))
    i += 1