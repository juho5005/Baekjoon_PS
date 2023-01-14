# 조합 0의 개수

# 0 <= m <= n <= 2,000,000,000
# O(1) : 시간 복잡도 유의

# nCm의 끝자리 0이 개수 출력

import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

# 총 곱해진 5의 개수 
def five(num) :
    cnt = 0

    while num != 0 :
        num //= 5 
        cnt += num 
    return cnt 

# 총 곱해진 2의 개수
def two(num) :
    cnt = 0
    while num != 0 :
        num //= 2
        cnt += num
    return cnt 

# n! // m! * (n-m)! 

print(min(five(n) - five(m) - five(n-m), two(n) - two(m) - two(n-m)))