# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러는 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요함
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test)
# if True
#     pass
# x => y

#  NameError : 참조변수 없음
a, b = 10, 15

# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3]) # 예외 발생

# KeyError
dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

# print(dic['hobby']) # direct access 
print(dic.get('hobby')) # 해당하는 키가 없으면 None 을 리턴 (권장)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time)
# print(time.month())   # 없는 메소스 참조

# ValueError : 참조값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10)    # 값이 없음
# x.index(10)

# FileNotFoundError
# f = open('test.txt', 'r')   # 파일 없어 예외

# TypeError
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) # 리스트와 튜플은 결합 불가 (예외)
# print(x + z)  # 리스트와 문자열은 결합 불가 (예외)

print( x + list(y) )    # 형변환

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩을 권장 (EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# ex 1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    # z = 'Zoe'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok else')


# ex 2
try:
    z = 'Kim'
    # z = 'Zoe'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: # 발생하는 에러가 무엇인지 모르는 경우
    print('Not found it! - Occurred Error!')
else:
    print('Ok else')


# ex 3
try:
    # z = 'Kim'
    z = 'Zoe'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('Ok else')
finally:    # 에러 발생 여부와 관계없이 무조건 마지막에 수행
    print('finally ok')


# ex 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok finally')


# ex 5
try:
    # z = 'Kim'
    z = 'Zoe'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l:
    print(l)
except IndexError as l:
    print(l)
except Exception:   # 나머지 에러
    print('Not found it! - Occurred Error!')
else:
    print('Ok else')
finally:   
    print('finally ok')


# ex 5
# 예외 발생 : raise
# raise 키워드로 예외를 직접 발생
try:
    a = 333
    # a = 'Kim'
    if a == 'Kim':
        print('ok 허가')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print('ok')

