#신조어 사전 만들기

#1번

word={'신조어1':'신조어1의 의미','신조어2':'신조어2의 의미','신조어3':'신조어3의 의미'}

print()
print("=======================================")
print("신조어 목록: 신조어1, 신조어2, 신조어3")
print("=======================================")
print()
choice=input("원하는 신조어를 입력하세요: ")
print("%s의 의미는 %s입니다." %(choice,word[choice]) )

#2번

word={'구취':'구독을 취소함','혼바비언':'혼밥 하는 사람','아바라':'아이스 바닐라 라떼'}

print()
print("===================================")
print("신조어 목록: 구취, 혼바비언, 아바라")
print("===================================")
print()
choice=input("원하는 신조어를 입력하세요: ")
print("%s의 의미는 %s입니다." %(choice,word[choice]) )

