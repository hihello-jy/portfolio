#문제3- 회문판별

def palindrome(word):
    n=len(word)
    if (n<2):
        return "True"
    elif word[0] != word[n-1]:
        return "False"
    else:
        return palindrome(word[1:n-1])

while True:
    word=input("문자열을 입력하세요: ")
    if word == "0":
        break
    else:
        print(palindrome(word))
    
print("프로그램을 종료합니다.")

#while문 밖에서 프로그램을 종료합니다해도되나?
#회문 예시 가장 최근 수업때 다뤘는데 그것도 한번더 보면 좋을 듯
