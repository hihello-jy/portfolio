print("<메뉴>")
print("1.아메리카노 3000원")
print("2.카페라떼 3500원")
print("3.카페모카 3800원")
print("4.종료")
print()
price=[3000,3500,3800]
total_price=0
sale_price = 0


for i in range(0,4):
    choice=int(input("번호 선택: "))
    if choice ==4:
        break
    else:
        cup=int(input("몇 잔?: "))
        total_price += (price[choice-1]*cup)

pay_price = total_price

if total_price >= 20000:
    sale_price=total_price*(10/100)
    pay_price= total_price-sale_price

print()
print("총액:",total_price)
print("할인액:",int(sale_price))
print("결재액:",int(pay_price))

#사실 이 코드에는결함이 있어 만약 누가 1,2,3,4말고 다른걸 누른다면? 그렇다면 4번 입력은 어떻게 해야하지?
