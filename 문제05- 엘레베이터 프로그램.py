def goDown():
    for i in range (current_floor-1,target_floor,-1):
        print ("현재 %d층 입니다." %(i))
    print("%d층에 도착하였습니다." %target_floor)

def goUP():
    for i in range (current_floor+1,target_floor):
        print ("현재 %d층 입니다." %(i))
    print("%d층에 도착하였습니다." %target_floor)

current_floor=int(input("현재 층: "))
target_floor=int(input("가는 층: "))
floor=[1,2,3,4,5]

if target_floor==current_floor or target_floor not in floor:
    print("다른층(1~5)을 눌러주세요.")

elif current_floor < target_floor:
    goUP()

else:
    goDown()
    
#값은 나오는데,, 이게 맞을까?
