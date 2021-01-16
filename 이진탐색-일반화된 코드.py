#ordering된 데이터 집합에서

a= []
flag = 0

n= int(input("입력할 숫자의 개수를 입력하세요: "))

for i in range(0,n,1):
    num = int(input("입력할 수를 입력하세요: "))
    a.append(num)

key= int(input("찾고자 하는 수를 입력하세요: "))

low = 0
high = n-1

for i in range (0,n,1):
    if low <= high: # low와 high가 자리를 바꾸지 않는다면,,
        mid= int((low+high)/2) #실수 값이 나올 수 도 있으니 정수화 시킴

        if key == a[mid]:
            print("인덱스", mid, "에서 탐색성공")
            flag =1
            break
        elif key < a[mid]: #찾고자하는 값이 mid보다 작으면
            high = mid-1
        else:              #찾고자하는 값이 mid보다 크면
            low= mid+1
    else:
        print("탐색실패")
        break
