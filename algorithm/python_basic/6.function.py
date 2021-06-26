# 함수식

# 함수 정의 방법
# def 함수명(parameter):
#   코드

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치가 중요함!

# ex1
def hello(world):
    print("Hello ", world)

hello("Python!")
hello(7777)

# ex2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str_1 = hello_return("python!!!!")
print(str_1)

# ex3 (다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

v1, v2, v3 = func_mul(100)
print(v1, v2, v3)

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]
    # return (y1, y2, y3)

lt = func_mul2(100)
print(lt, type(lt))

#ex4
# *args, *kwargs   

# * : 인자가 튜플 형태로 넘어감
def args_func(*args):
    for i, v in enumerate(args):
        print(i, v)
    # for t in args:
    #     print(t)
    # print(type(args))

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')

# ** : 인자가 딕셔너리 형태로 넘어감
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    # print(kwargs)

kwargs_func(name1="Kim", name2="Park")

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', age=24, age2=35)

# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# ex6 (hint 사용)
def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))


