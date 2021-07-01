# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로

# 파일 읽기
# ex 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close하여 리소스 반환
f.close()

print('-----------------------')

# ex 2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    # print(list(c))
    print(iter(c))

print('-----------------------')

# ex 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) # \n 제거


# ex 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()     # 빈내용 (한번에 데이터 읽어옴)
    print(">", content)    # 내용없음

print('-----------------------')
print('-----------------------')


# ex 5
with open('./resource/review.txt', 'r') as f:
    line = f.readline() # 한줄씩 읽기
    # print(line)
    while line:
        print(line, end=' ')
        line = f.readline()

print('\n-----------------------')

# ex 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()    # readlines : 개행문자(\n)을 기준으로 리스트 형식으로 read
    print(contents)
    for c in contents:
        print(c, end=' ***')

print('-----------------------')
print('-----------------------')

# ex 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기
# ex 1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman\n')

# ex 2

with open('./resource/text1.txt', 'a') as f:
    f.write('Goodboy\n')

# ex 3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(0, 50)))    # 0 ~50 사이의 숫자 랜덤하게 쓰기
        f.write('\n')

# ex 4
# writelines : 리스트를 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# ex 5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contents1 !!! ', file=f)
    print('Test Contents2 !!! ', file=f)