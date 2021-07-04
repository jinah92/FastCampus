# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 메소드, 인스턴스 메소드, static 메소드

# 기본 인스턴스 메소드

class Student(object):
    '''
    Student Class
    Author : Kim
    Date : 2019.07.25
    Description : Class, Static, Instance Method
    '''

    # Class Variable
    tuition = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa) -> None:
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method (인자값이 self로 시작되는 메소드)
    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    # Instance Method (인자값이 self로 시작되는 메소드)
    def detail_info(self):
        return f'Student Detail Info : {self._id}, {self.full_name()}, {self._email}, {self._grade}, {self._tuition}, {self._gpa}'
    
    # Instance Method
    def get_fee(self):
        return f'Before Tuition -> ID: {self._id} {self._tuition}'

    # Instance Method
    def get_fee_culc(self):
        return f'After Tuition -> ID: {self._id} {self._tuition * Student.tuition}'

    def __str__(self) -> str:
        return f'Student Info -> name: {self.full_name()}, grade: {self._grade}, email: {self._email}'

    # class method
    @classmethod
    def raise_fee(cls, per):    # 첫번째 인자(cls) : class
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.tuition = per
        print("Success!")

    # class method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition, gpa)
    
    # static method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return f'{inst._last_name} is a scholaship recipient'
        return 'Sorry. Not a scholaship'

student_1 = Student(1, 'Kim', 'Sarang', 'student@naver.com', 1, 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student@daum.net', 2, 500, 4.3)

# 기본 정보
print(student_1)
print(student_2)

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보 (인상 전)
print(student_1.get_fee())
print(student_2.get_fee())

# 학비 인상 (클래스 메소드 미사용)
Student.tuition = 1.2
# 학비 정보 (인상 후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

# 클래스 메소드 사용
Student.raise_fee(1)

print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

# 클래스 메소드 인스턴스 생성
student_3 = Student.student_const(3, 'Park', 'Minji', 'student@gmail.com', 3, 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Sunghan', 'student44@gmail.com', 4, 600, 4.1)

# 전체 정보
print(student_3.detail_info())
print(student_4.detail_info())

# 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)

# 장학금 혜택 여부(static method 미사용)
def is_scholaship(inst):
    if inst._gpa >= 4.3:
        return f'{inst._last_name} is a scholaship recipient'
    return 'Sorry. Not a scholaship'

print(is_scholaship(student_1))
print(is_scholaship(student_2))
print(is_scholaship(student_3))
print(is_scholaship(student_4))

print()

# 장학금 혜택 여부(static method 사용)
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()
# 장학금 혜택 여부(static method 사용)
print(student_1.is_scholarship_st(student_1))
print(student_1.is_scholarship_st(student_2))
print(student_1.is_scholarship_st(student_3))
print(student_1.is_scholarship_st(student_4))
