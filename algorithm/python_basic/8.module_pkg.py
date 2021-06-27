# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
#  .. : 부모 디렉터리
#  . : 현재 디렉토리

# 사용 1 (클래스 형태)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print('ex2: ', Fibonacci.fib2(400))
print('ex3: ', Fibonacci().title)


# 사용 2 (클래스) - 권장하지 않음. 메모리 비효율
from pkg.fibonacci import *

Fibonacci.fib(300)

print('ex2: ', Fibonacci.fib2(400))
print('ex3: ', Fibonacci().title)


# 사용 3 (클래스) - alias 사용
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)

print('ex2: ', fb.fib2(400))
print('ex3: ', fb().title)


# 사용 4 (함수)
import pkg.cal as c

print('ex4: ', c.add(10, 100))
print('ex5: ', c.mul(10, 100))


# 사용 5 (함수)
from pkg.cal import div as d
print('ex6: ', int(d(100, 10)))


# 사용 6 (함수)
import pkg.prints as p
import builtins # 파이썬 내장모듈
p.prt1()
p.prt2()
print(dir(builtins))