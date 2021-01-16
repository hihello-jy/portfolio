#소문자! aeiou의 개수를 각각 출력하는 프로그램.
#문자열은 영문 알파벳만 입력한다고 가정하자.

aeiou=['a','e','i','o','u']
text=input("문자열을 입력하세요: ")

found={}

found['a']=0
found['e']=0
found['i']=0
found['o']=0
found['u']=0

for letter in text:
    if letter in aeiou:
        found[letter] += 1

for k,v in sorted(found.items()):
    print('%s: %d' %(k,v),end=', ')
