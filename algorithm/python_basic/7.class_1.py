# 파이썬 클래스
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후에 사용

# 선언 방식
# class 클래스명:
#     함수
#     함수

# ex1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
        # print("초기화: ", name)
    def user_info_p(self):
        print("Name: ", self.name)


user1 = UserInfo('mina')
user1.user_info_p()
user2 = UserInfo('park')
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# ex2
# self의 이해
class SelfTest:
    def function1():        # self (x) => 클래스 메소드
        print('function1 called!')
    def function2(self):    # 인스턴스 메소드
        print(id(self))
        print('function2 called!')
    
self_test = SelfTest()
SelfTest.function1()
self_test.function2()

# SelfTest.function2()    # error
SelfTest.function2(self_test)

# ex3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kimm')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__)   # 클래스 네임스페이스, 클래스 변수 (공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)  # 자신의 네임스페이스에 없으면 클래스 네임스페이스에서 변술르 찾음. 거기도 없으면 에러가 발생
print(user2.stock_num)
print(user3.stock_num)

del user1               # 인스턴스 삭제(del)

print(user2.stock_num)  # 클래스 변수 (stock_num) 이 하나 줄음
print(user3.stock_num)
