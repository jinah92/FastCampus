# 해시테이블 => 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict => key 충복 허용 x, Set -> 중복 허용 x
# Dict 및 Set 심화

# Dict 구조
print('EX1-1 -')
print(__builtins__.__dict__)

print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print('EX1-2 -', hash(t1))
# print('EX1-3 -', hash(t2)) # error : 가변형 데이터인 리스트가 포함되어 있음

print()

# 지능형 딕셔너리(Comprehending Dict)
import csv

# 외부 csv 파일을 tuple형태의 리스트로 변환
with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print('EX2-1 -')
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('EX2-2 -')
print(n_code1)

print()
print()

print(n_code2)

print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
            ('k1', 'val2'), # key 중복
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))
        
new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('EX3-1 -', new_dict1)

# use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)   # 없으면 k, 있으면 빈 리스트

print('EX3-2 -', new_dict2)

# 사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print("Called: __missing__")
        if isinstance(key, str):    #문자열인 경우
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        print("Called: __getitem__")
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        print("Called: __contains__")
        return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one':1, 'two':2})
user_dict3 = UserDict([('one', 1), ('two', 2)])

# 출력
print('EX4-1 -', user_dict1, user_dict2, user_dict3)
print('EX4-2 -', user_dict1.get('two'))
print('EX4-2 -', user_dict1.get('aaa')) # 없는 키를 조회 => __missing__ 메소드 실행
print('EX4-3 -', 'one' in user_dict2)   # __contains__ 메소드 실행 (값이 있는 경우 True, 아니면 False)
# print(user_dict3['three'])  # key error
print('EX4-5 -', user_dict3.get('three'))
print('EX4-6 -', 'three' in user_dict3)

print()
print()

# immutable Dict

from types import MappingProxyType

d = {'key1': 'TEST1'}

# read only
d_frozen = MappingProxyType(d)

print('EX5-1 -', d, id(d))
print('EX5-2 -', d_frozen, id(d_frozen))
print('EX53 -', d is d_frozen, d == d_frozen) # id비교, 값 비교

# 수정 불가
# d_frozen['key1'] = 'TEST2'

d['key2'] = 'TEST2' #원본은 수정 가능
print('EX5-4 -', d)
print()
print()

# set 선언
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')

# 추가불가 (frozenset)
# s5.add('Melon') # error

print('EX6-1 -', s1, type(s1))
print('EX6-2 -', s2, type(s2))
print('EX6-3 -', s3, type(s3))
print('EX6-4 -', s4, type(s4))
print('EX6-5 -', s5, type(s5))

# 선언 최적화
from dis import dis

print('EX6-5 -')
print(dis('{10}'))

print('EX6-6 -')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name

print('EX7-1 -')
print({name(chr(i), '') for i in range(0, 256)})

