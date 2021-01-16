#문제04-주사위 100번 나오는 값들의 빈도 계산하기

import random
count_dice=[0,0,0,0,0,0]
dice=[1,2,3,4,5,6]
for i in range (0,100):
    num=random.choice(dice)
    count_dice[num-1] += 1

for i in range(0,6):
    print("주사위 %d: %d" %(i+1,count_dice[i]))
