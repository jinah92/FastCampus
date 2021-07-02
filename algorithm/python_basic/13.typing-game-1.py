# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성
import random
import time

words = [] # 영어 단어 리스트 (1000개 로드)

n = 1       # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip()) # 양쪽 공백을 제거
    
# print(words)    # 단어 리스트 확인

input('Ready? Press Enter Key!')

start = time.time()

while n <= 5:
    random.shuffle(words) # shuffle - 단어의 순서를 임의대로 섞음
    q = random.choice(words)    # 랜덤으로 단어를 뽑아옴 

    print()
    print('Question # {}'.format(n))
    print(q)    # 문제 출력

    x = input() # 타이핑 입력
    print()
    
    if str(q).strip() == str(x).strip():    # 입력값 비교 (공백 제거)
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("탈락")

# 수행시간 출력
print("게임 시간 : ", et, "초 ", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass


