
def add (num1,num2):
    sum= num1+ num2
    return sum
    
def subtract (num1,num2):
    if num1>num2:
        answer= num1-num2
        return answer
    elif num1<num2:
        answer= num2-num1
        return answer
    else:
        return 0.0

def multiply (num1,num2):
    answer= num1*num2
    return answer

def division (num1,num2):
        answer=num1/num2
        return answer
    
    
while(1):
    num1 = float(input("첫번째 수를 입력하세요: "))
    num2 = float(input("두번째 수를 입력하세요: "))
    print("종료:0, 덧셈:1, 뺄셈:2, 곱셈:3, 나눗셈:4")
    choice=int(input("원하는 계산을 선택하세요: "))

    if choice ==0:
        print("프로그램을 종료합니다.")
        break
    elif choice ==1:
        print("Result = ", add(num1,num2))
    elif choice ==2:
        print("Result = ", subtract(num1,num2))
    elif choice==3:
        print("Result = ", multiply(num1,num2))
    elif choice==4:
        if num2==0:
            print("0으로 나눌 수가 없습니다. 다시 시작합니다.")
            continue
        else:
            print("Result = ", division(num1,num2))

    else: # 과제에서는 이 부분이 자세히 나와있지 않지만, 사용자가 0,1,2,3,4 가 아닌 다른 걸 입력했을 때 오류메세지와 함께 처음부터 다시 시작할 수 있도록 하였다.
        print("잘못 입력하셨습니다.(0~4 중에서 선택하세요.) 계산기 프로그램을 다시 시작합니다.")
        continue
        
