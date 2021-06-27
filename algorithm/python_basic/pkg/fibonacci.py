class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title
    
    def fib(n):     # 피보나치 수열을 출력하는 함수
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fib2(n):    # 피보나치 수열을 담은 배열을 리턴하는 함수
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result