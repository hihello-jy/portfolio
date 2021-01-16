n=int(input("정수(>=2)를 입력하세요: "))

if n<2:
    print("잘못 입력하였습니다.")

else:
    for i in range (2,n+1,1):
        flag=True
        for s in range (2,i,1):
            if i%s == 0:
                flag= False
                break

        if flag== True:
            print(i,end=' ')
