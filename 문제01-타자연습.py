#문제01-타자연습

import random
word=['cat','dog','rabbit','duck','dolphin','wolf','raccoon','monkey'] #조건1
n=0
c=0
flag=0

input("타자게임 시작(엔터입력):" )

while True:
    if flag == 1:
        break
    a=random.choice(word)#조건2
    print ("(종료 0):",a)
    b= input("입력: ")
    if a == b:
        print("맞음!!")
        n += 1
        c += 1
        
    elif b == "0" :
        break
    else:
        print ("오타! 다시 도전!")
        n += 1
        while True:
            print("(종료 0):",a)
            b= input("입력: ")
            n += 1
            if a == b:
                print("맞음!!")
                c += 1
                break
            elif b=="0":
                flag=1
                break
            else:
                print ("오타! 다시 도전!")

correct_number= c
correct_percentage= (c / n)*100

print("맞은개수: %d, 정답률: %4.1f" %(correct_number,correct_percentage))
