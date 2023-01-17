# 10진수 N이 주어질 때 
# 이 수를 B진법으로 바꿔 출력하는 프로그램 작성

import sys 
n, b = tuple(map(int, sys.stdin.readline().split()))
# 2 <= b <= 36
# 1 <= n <= 1,000,000,000 
# n에 대하여 시간복잡도 고려 대상 

matching = {}
alpha_start = 65
for i in range(10, 37) :
    matching[i] = chr(alpha_start)
    alpha_start += 1

ans = ''

while n != 0 :
    res = n%b

    if res >= 10 : 
        ans = str(matching[res]) + ans
    else :
        ans = str(res) + ans
    n //= b 
print(ans)