# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))
print(type(v_set))
print(type(v_list))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999999
bit_int2 = 7777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * bit_int2)
print(f1 ** f2)
result = f3 + i2
print(result, type(result)) # float 형변환

a = 5.  # float
b = 4   # int
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형 변환 (int, float, complex)
print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

y = 100
y *= 100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))
n, m = divmod(100, 8)   # 몫은 n, 나머지는 m에 할당
print(n, m)

import math

print(math.ceil(5.1))   # 인자보다 큰 정수 중 가장 작은 정수
print(math.floor(3.874))    # 인자 이하의 수 중 가장 작은 정수