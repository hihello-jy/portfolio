a=[]
flag =0

n= int(input("입력할 숫자의 개수를 입력하세요: "))

for i in range(0,n,1):
    num = int(input("입력할 수를 입력하세요: "))
    a.append(num)

key= int(input("찾고자 하는 수를 입력하세요: "))

for cnt in range(0,n,1):
    if key == a[cnt]:
        print("인덱스", cnt, "에서 탐색 성공")
        flag = 1
        break

if flag ==0:
    print ("탐색 실패")
