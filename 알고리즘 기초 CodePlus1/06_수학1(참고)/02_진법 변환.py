# B진법 수 N이 주어지고 
# 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성

import sys 
# 2 <= b <= 36

n, b = sys.stdin.readline().rstrip().split()
b = int(b)


matching = {}
alpha_start = 65
for i in range(10, 37) :
    matching[chr(alpha_start)] = i
    alpha_start += 1

idx = 0 
res = 0 
for elem in n[::-1] :
    if ord(elem) >= 65 and ord(elem) <= 90 : 
        res += (ord(elem)-55) * (b**idx)
    else :
        res += int(elem) * (b**idx)
    idx += 1

print(res)