americano_price=2000
cafelatte_price=3000
capucino_price=3500

americanos=int(input("아메리카노 판매 개수: "))
cafelattes=int(input("카페라떼 판매 개수: "))
capucinos=int(input("카푸치노 판매 개수: "))

sales=americanos*americano_price
sales=sales+cafelattes*cafelatte_price
sales=sales+capucinos*capucino_price

print("총 매출은 "+str(sales)+"입니다")


profit=sales-100000
print("순이익은",profit,"입니다")
