def palindrome(word):
    n=len(word)
    if (n<2):
        return "회문입니다."
    elif word[0] != word[n-1]:
        return "회문이 아닙니다."
    else:
        return palindrome(word[1:n-1])

word=input("문자열을 입력하세요: ")
print(palindrome(word))
