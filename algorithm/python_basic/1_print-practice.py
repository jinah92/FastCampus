# 파이썬 기초 코딩
# print 구문 예제

# 기본 출력
print('HELLO PYTHON')
print("HELLO PYTHON")
print("""HELLO PYTHON""")
print('''HELLO PYTHON''')

print()

# Seperator 옵션
print('T', 'E', 'S', 'T', sep='')   # TEST
print('2019', '02', '19', sep='-')  # 2019-02-19
print('niceman', 'google.com', sep='@') # niceman@google.com

# end 옵션 사용 
print('Welcom To', end='')             # Welcom To the black parade piano notes
print(' the black parade', end='')
print(' piano notes')

print()

# format 사용
print('{} and {}'.format('You', 'Me'))  # You and Me
print("{0} and {1} and {0}".format('You', 'Me'))    # You and Me and You
print("{a} are {b}".format(a='You', b='Me'))    # You and Me

print("%s's favorite number is %d" %('Jinah', 3)) # %s : 문자, %d : 정수, %f : 실수

# Test1:   776, Price:  6523.12
print("Test1: %5d, Price: %4.2f" %(776, 6534.123)) # %5d : 5자리 정수, %4.2f : 4자리 정수 + 소수 둘째짜리
print("Test1: {0: 5d}, Price: {1:4.2f}".format(776, 6523.123))
print("Test1: {a: 5d}, Price: {b:4.2f}".format(a=776, b=6534.123))


'''
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
'''

print("'you'")      # 'you'
print('\'you\'')    # 'you'
print('"you"')      # "you"
print("""'you'""")  # "you"
print('\\you\\\n')
print('\t\t\ttest')