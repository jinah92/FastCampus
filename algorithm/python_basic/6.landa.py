# 람다식
# 람다식: 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num*10

var_func = mul_10   # 함수를 메모리에 할당
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda num: num * 10
print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

func_final(10, 10, lambda x : x * 1000)