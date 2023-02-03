# 정수 n이 주어질 때 
# n을 1, 2, 3의 합으로 나타내는 방법의 수는 ?

import sys 
t = int(sys.stdin.readline())

dp = [0, 1, 2, 4]

# n < 11 이므로 dp를 미리 구해놓는다
for i in range(4, 11) :
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for _ in range(t) :
    n = int(sys.stdin.readline())

    print(dp[n])
    