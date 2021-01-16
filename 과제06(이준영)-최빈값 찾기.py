from collections import Counter

def findMax(numbers):
    c=Counter(numbers)
    numbers_freq=c.most_common()
    max_count=numbers_freq[0][1]

    modes=[]
    for num in numbers_freq:
        if num[1]==max_count:
            modes.append(num[0])
    max_value=modes[-1]
    return max_value
    

a1=[1,2,3,4,3,5,2,5,3]
a2=[1,2,3,5,3,5,2,5,3]

print(a1,findMax(a1))
print(a2,findMax(a2))
