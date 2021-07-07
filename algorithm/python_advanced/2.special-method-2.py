# 매직메소드 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스, 반복, 함수, 클래스

# 매직메소드 기초 설명

# 기본형
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))

print()

n = 100

# 사용
print('EX1-1 -', n + 200)
print('EX1-2 -', n.__add__(200))
print('EX1-3 -', n.__doc__)
print('EX1-4 -', n.__bool__(), bool(n))
print('EX1-5 -', n * 100, n.__mul__(100))

print()

# 클래스 예제 1
class Student:
    def __init__(self, name, height) -> None:
        self._name = name
        self._height = height

    def __str__(self) -> str:
        return f'Student Class Info : {self._name, self._height}'

    def __ge__(self, x):
        print('Called >> ___ge__')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> ___le__')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> ___sub__')
        return abs(self._height - x._height)


# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

# print(s1 + s2) # error
print(s1._height > s2._height)

# 매직메소드 출력
print('EX2-1 -', s1 >= s2)
print('EX2-2 -', s1 <= s2)
print('EX2-3 -', s1 - s2)
print('EX2-3 -', s2 - s1)

print()

# 클래스 예제2
class Vector(object):
    def __init__(self, *args) -> None:
        '''Create a Vector, example : v = Vector(1,2)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
    
    def __repr__(self):
        '''Return the vector information'''
        return 'Vector(%r %r)' %(self._x, self._y)
    
    def __add__(self, other):
        '''Return the vector addtion of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직메소드 출력
print('EX3-1 -', Vector.__init__.__doc__)
print('EX3-2 -', Vector.__repr__.__doc__)
print('EX3-4 -', Vector.__add__.__doc__)
print('EX3-3 -', v1, v2, v3)
print('EX3-5 -', v1 + v2)
print('EX3-6 -', v1 * 4)
print('EX3-7 -', v2 * 10)
print('EX3-8 -', bool(v1), bool(v2))
print('EX3-9 -', bool(v3))

