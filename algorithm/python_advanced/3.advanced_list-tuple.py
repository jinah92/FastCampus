# 시퀀스형
# 컨테이너(container) : 서로 다른 자료형(list, tuple, collections.deque)을 저장
# Flat : 한 개의 자료형(str, bytes, bytearray, array.array, memoryview)만 저장
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트 (Comprehending List)

# Non-Comprehending List
chars = '!@#$%^&*()_+'
code1 = []

for s in chars:
    code1.append(ord(s))

# Comprehending list (상대적으로 빠른 속도)
code2 = [ord(s) for s in chars]

# Comprehending list (더 빠른 속도)
code3 = [ord(s) for s in chars if ord(s) > 40]
code4 = list(filter(lambda x : x > 40, map(ord, chars)))    # map, filter 결합

print('EX1-1 -', code1)
print('EX1-2 -', code2)
print('EX1-3 -', code3)
print('EX1-4 -', code4)
print('EX1-5 -', [chr(s) for s in code4])

print()

# Generator
import array

# Generator : 한 번에 한 개의 항목을 생성 (메모리 유지 x)
tuple_g = (ord(s) for s in chars)
# Array
array_g = array.array('I', (ord(s) for s in chars))

print('EX2-1 -', tuple_g)
print('EX2-2 -', next(tuple_g))
print('EX2-3 -', next(tuple_g))
print('EX2-4 -', array_g)
print('EX2-4 -', array_g.tolist())

print()

# 제너레이터 예제
print('EX3-1 -', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print('EX3-2 -', s)

# 리스트 주의할 점
marks_1 = [['~'] * 3 for n in range(3)]
marks_2 = [['~'] * 3] * 3

print('EX4-1 -', marks_1)
print('EX4-2 -', marks_2)

marks_1[0][1] = 'X'
marks_2[0][1] = 'X'

print('EX4-3 -', marks_1)
print('EX4-4 -', marks_2) # ERROR

# 증명
print('EX4-5 -', [id(i) for i in marks_1])
print('EX4-6 -', [id(i) for i in marks_2]) # 모두 동일한 주소값을 바라봄

# Tuple Advanced
# Pcking & Unpacking

a, b = divmod(100, 9)   # 변수 할당 시, Unpacking
print(a, b)

print('EX5-1 -', divmod(100, 9))
print('EX5-2 -', divmod(*(100, 9)))
print('EX5-3 -', *(divmod(100,9)))

print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest)
x, y, *rest = range(2)
print('EX5-5 -', x, y, rest)
x, y, *rest = 1,2,3,4,5
print('EX5-6 -', x, y, rest)

print()

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, m)
print('EX6-2 -', l, m, id(l), id(m))

# 재할당
l = l * 2
m = m * 2

print('EX6-2 -', l, m, id(l), id(m))
# l[0] = 3 # error (수정 불가)

# 내부 수정
l *= 2
m *= 2

print('EX6-2 -', l, m, id(l), id(m))
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객체를 반환

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))  # 내림차순
print('EX7-3 -', sorted(f_list, key=len))  # 글자 길이순서대로 정렬
print('EX7-4 -', sorted(f_list, key=lambda x:x[-1]))  # 마지막 글자 순으로 정렬

print('EX7-5 -', f_list)    # 원본은 유지
print()

# sort : 정렬 후 객체 직접 변경
# 반환 괎 확인 : None

a = f_list.sort()
print('EX7-6 -', f_list.sort(), f_list)
print('EX7-7 -', f_list.sort(reverse=True), f_list)
print('EX7-8 -', f_list.sort(key=len), f_list)
print('EX7-9 -', f_list.sort(key=lambda x:x[-1]), f_list)
print('EX7-10 -', f_list.sort(key=lambda x:x[-1], reverse=True), f_list)
