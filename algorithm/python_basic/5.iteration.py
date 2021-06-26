# 반복문
# 파이썬 기본 반복문: for, while

v1 = 1
while v1 < 11:
    print("v1 is: ", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is: ", v2)

for v3 in range(1, 11):
    print("v3 is: ", v3)

# 1 ~ 100 까지의 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100: ', sum1)
print('1 ~ 100: ', sum(range(1, 101)))
print('1 ~ 100: ', sum(range(1, 101, 2)))   # 2개씩 증가

# 시퀀스(순서가 있는) 자료형을 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ["kim", "park", "cho", "choi", "yoo"]
for name in names:
    print(name)

word = "dreams"
for s in word:
    print(s)

my_info = {
    "name": "kim",
    "age": 33,
    "city": "seoul"
}

for key in my_info:
    print("my_info: ", key)

for key in my_info.values():
    print("my_info: ", key)

for key in my_info.keys():
    print("my_info: ", key)

for k, v in my_info.items():
    print("my_info: ", k, v)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found 33")
        break
    else:
        print("not found 33")

# for -else 구문
# 반복문이 정상적으로 수행된 경우, else 블럭을 실행
for num in numbers:
    if num == 40:
        print("found 40")
        break
    else:
        print("not found 40")
else:
    print("not found 40 .... ")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print('type: ', type(v))

# 자료구조 변환
name = "Niceman"
print(list(reversed(name)))
print(tuple(reversed(name)))