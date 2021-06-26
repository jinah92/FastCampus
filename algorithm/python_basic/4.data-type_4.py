# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서 x, 중복 x, 수정 o, 삭제 o
# key, value (JSON) -> MongoDB 등에서 사용하는 포맷

# 선언방법
a = {'name': 'kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}
# print(type(a))

# 출력
# print(a['name1'])   # 없는 key일 경우 에러발생
print(a.get('name'))  # get메소드로 접근 (없으면 None을 리턴) => 보다 안전한 key 접근방법
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3,)
print(a)

# keys, values, items (=key와 value 쌍)
print(a.keys()) # key만 리스트 형태로 반환
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])    # (중요) key 배열에 접근하려면 list 형변환이 필요

print(a.values())
print(list(a.values()))

print(list(a.items()))
print(1 in b)   # key의 존재여부 확인 (True, False)


# 집합(set) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)    # 중복값을 없앤 결과를 리턴

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집홥
print(s1.intersection(s2)) 
print(s1 & s2)

# 합집합
print(s1 | s2)  
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7)   # 중복되어 업데이트되지 않음
print(s3)

s3.remove(15)
print(s3)


