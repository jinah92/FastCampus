# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩 (3.xx 버전): 파이썬은 기본입출력이 UTF-8 인코딩 되어있다.
print(sys.stdin.encoding)   # UTF-8
print(sys.stdout.encoding)   # UTF-8

# 출력문
print("My name is Good girl")

# 변수 선언
my_name = 'Good girl'

# 조건문
if my_name == 'Good girl':
    print('ok')

# 반복문 (구구단 출력)
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' %(i, j), i*j)

# 변수 선언(한글)
이름 = "좋은사람"

# 출력
print(이름)

# 함수 선언
def greeting():
    print('hello!')

greeting() # 함수 실행

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))