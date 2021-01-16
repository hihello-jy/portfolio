#서로 다른 세 개의 양의 정수를 입력 받는다는 전제가 있다.

a=int(input("첫 번째 정수를 입력하세요: "))
b=int(input("두 번째 정수를 입력하세요: "))
c=int(input("세 번째 정수를 입력하세요: "))

if a>b and a>c:
    max=a

elif b>a and b>c: # 그냥 b>c라고 해도 괜찮다.
    max=b

else:
    max=c

print("%d이 가장 큽니다." %(max))
