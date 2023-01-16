# 2진수가 주어졌을 때 8진수로 변환하는 프로그램 작성

import sys 
binary_nums = sys.stdin.readline().rstrip() # 2진수 입력 

lst = [
    int(elem)
    for elem in binary_nums
]

if len(lst) % 3 == 2 : 
    lst.insert(0, 0)
elif len(lst) % 3 ==  1:
    for _ in range(2) :
        lst.insert(0, 0)
else :
    pass 


# 결과
res = ''

for i in range(0, len(lst), 3) :
    res += str( (lst[i] * (2**2)) + (lst[i+1] * (2**1)) + lst[i+2] * (2**0))

print(res)