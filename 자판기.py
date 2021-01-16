money=int(input("투입한 돈: "))
price=int(input("물건값: "))
change=money-price
print("거스름돈:",change)

x=change//500
y=(change%500)//100


print("500원 동전의 개수:",x)
print("100원 동전의 개수:",y)

#자판기가 만약 50원짜리 동전과 10원짜리 동전도 거슬러 줄 수 있다면 위의 코드를 어떻게 수정해야하는가?
