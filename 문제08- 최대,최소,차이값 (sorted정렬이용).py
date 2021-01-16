score=[95,88,50,20,78,56,67,90,36,49]
scr=sorted(score)

def high_score(): #최대값을 구하는 함수
    return scr[-1]

def low_score(): #최소값을 구하는 함수
    return scr[0]

def gap_score(): #최대값과 최소값의 차이를 구하는 함수
    return (scr[-1]-scr[0])

print("최댓값: %d 최소값: %d 차이값: %d" %(high_score(),low_score(),gap_score()))
