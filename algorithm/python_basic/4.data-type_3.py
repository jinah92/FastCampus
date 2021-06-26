# 리스트, 튜플

# 리스트 (순서 o, 중복 o, 수정 o, 삭제 o)
# 선언방식
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 1000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 리스트 마지막에 요소를 추가
print(y)
y.sort()     # 오름차순 정렬
print(y)   
y.reverse() # 내림차순 정렬
print(y)
y.insert(2, 7)  # 2번 인덱스에 7을 삽입
print(y)
y.remove(2) # 2 인 요소를 삭제
y.remove(7)
print(y)
y.pop()     # 마지막부터 리스트를 하나씩 삭제 (LIFO)    - 비어잇는 경우 error
print(y)
ex = [88, 77]
y.append(ex)    # 리스트 자체를 삽입
# y.extend(ex)  # 요소로 삽입
print(y)

# 삭제 : del, remove, pop

# 튜플 (순서 o, 중복 o, 수정 x, 삭제 x)
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2]    # error: 삭제불가
print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)    # 하나의 튜플로 반환
print(c * 3)
print()

# 튜플 함수
z = (5, 2, 1, 3, 4)
print(z)
print(3 in z)
print(z.index(3))   # 3이 있는 곳의 인덱스를 반환
print(z.index(5))
print(z.count(1))   # 1의 개수를 반환