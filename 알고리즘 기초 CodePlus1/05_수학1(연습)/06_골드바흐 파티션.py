# 골드바흐의 추측
# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션
# 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자
# 순서가 다른 쌍은 고려 x 

# python3로는 시간초과가 발생하여 pypy3로 제출하였다.

import sys 
import math 
t = int(sys.stdin.readline()) # 1 <= T <= 100 
# O(N^4)

# 에라토스테네스의 체
prime_nums = [
    True 
    for i in range(1000001)
]
prime_nums[0] = False 
prime_nums[1] = False 

for i in range(2, int(math.sqrt(1000000))+1) :
    j = 2
    if prime_nums[i] :
        while i*j <= 1000000 : 
            prime_nums[i*j] = False 
            j += 1 

for _ in range(t) :
    n = int(sys.stdin.readline()) # 2 < N <= 1,000,000 
    # n의 시간복잡도를 고려하여 에라토스테네스의 체 사용

    # 골드바흐 파티션의 수 
    cnt = 0 
    
    for i in range(2, n//2 + 1) : # 0과 1은 소수가 아니므로 2부터 비교 시작
        if prime_nums[i] and prime_nums[n-i] :
            cnt += 1
    
    print(cnt)