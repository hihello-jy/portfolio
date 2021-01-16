import random
count=0
guess=0
answer= random.randint(1,100)
print("컴퓨터 생성 숫자: %d" %answer)


while guess==answer:
    guess=int(input("1~100 사이의 숫자를 맞춰보세요:"))
    count += 1
    if guess>answer:
        print("높음")
    elif guess<answer:
        print("낮음")
    else:
        print("정답은 %d입니다." %answer)
        print("축하합니다. 시도횟수는 %d입니다." %count)
