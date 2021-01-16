year=["원숭이","닭1","개","돼지","쥐","소","호랑이","토끼","용","뱀","말","양"]

birth_year=int(input("태어난 연도를 입력하세요: "))
num= birth_year % 12

animal=year[num]

print("태어난 연도는 %d 년이며, %s 띠입니다." %(birth_year,animal))
