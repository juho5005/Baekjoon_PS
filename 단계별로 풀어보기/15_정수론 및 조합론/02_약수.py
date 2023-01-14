# 양수 A가 N의 진짜 약수가 되려면
# N이 A의 배수이고 A가 1, N이 아니여야 한다

import sys 
n = int(sys.stdin.readline()) # n <= 50 (자연수)

divisor = list(map(int, sys.stdin.readline().split()))

min_divisor = min(divisor)
max_divisor = max(divisor)

print(min_divisor * max_divisor)