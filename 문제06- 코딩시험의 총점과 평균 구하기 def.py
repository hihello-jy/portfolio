#문제06-코딩시험 총점과 평균을 출력

def total():
    global t
    t=0
    for i in range (0,5):
        t += scorelist[i]
    return t
    
def avg(): return (t/5)
#average함수가 이걸ㄹ로 해도 되나 싶지만,,,,,ㅎㅎㅎㅎㅎㅎ
    
scorelist=[]
while True:
    score=int(input("점수를 입력하세요: "))
    if score<0 or score>100:
        print("유효한 점수가 아닙니다.")
    else:
        scorelist.append(score)
        if len(scorelist)==5:
            break

print("합계: ",total())
print("평균: ",avg())
        
#일단 답은 그대로 나왔지만, 다시 생각해보기
