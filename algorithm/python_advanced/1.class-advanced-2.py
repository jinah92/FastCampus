# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    '''
    Student Class
    Author : Kim
    Date : 2019.05.25
    '''

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None) -> None:
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1
    
    def __str__(self) -> str:
        return f'str {self._name}'

    def __repr__(self) -> str:
        return f'repr {self._name}'
    
    def detail_info(self):
        print(f'Current ID: {id(self)}')
        print(f'Student Detail Info : {self._name} {self._email} {self._details}')

    def __del__(self):
        Student.student_count -= 1


# Self 의미
studt1 = Student('Cho', 2, 3, {'gender' : 'Male', 'score1': 50, 'score2' : 44}, 'test@gmail.com')
studt2 = Student('Cho', 2, 3, {'gender' : 'Male', 'score1': 50, 'score2' : 44}) # 다른 id
# studt2 = Student('Lee', 4, 1, {'gender' : 'Femal', 'score1': 90, 'score2' : 80})

a = 'ABC'
b = a

# 각 인스턴스의 id를 비교
print(id(studt1))
print(id(studt2))

print(studt1._name == studt2._name) # 값의 비교
print(studt1 is studt2) # id 비교
print(a is b)  # 같은 id를 공유
print(a == b)

# dir & __dict__ 확인 (속성값 확인)
print(dir(studt1))
print(dir(studt2))
print(studt1.__dict__)
print(studt2.__dict__)

# Doctsring   (클래스의 주석 확인)
print(Student.__doc__)

# 실행
studt1.detail_info()
studt2.detail_info()

# 에러
# Student.detail_info()

Student.detail_info(studt1) # 클래스로 직접 메소드를 접근 (인스턴스화된 변수를 이용)
Student.detail_info(studt2)

# 비교
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__) == id(studt2.__class__)) # 동일 클래스 (True)

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장 X)

# studt1._name = 'ㅋㅋㅋ' # 직접 접근하여 값 변경
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

# 클래스 변수 (누구나 접근이 가능 - 클래스, 인스턴스)
print(studt1.student_count, studt2.student_count)
print(Student.student_count)


# 공유 확인
print(Student.__dict__)
print(studt1.__dict__) # student_count (클래스 변수) 없음
print(studt2.__dict__) # student_count (클래스 변수) 없음

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성이 가능 (인스턴스 검색 -> 상위(클래스 변수, 부모 클래스 변수))

del studt2

print(studt1.student_count)
print(Student.student_count)