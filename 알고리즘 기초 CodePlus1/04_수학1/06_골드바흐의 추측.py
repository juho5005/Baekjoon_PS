# 골드바흐의 추측
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있음
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램 작성

import sys 
import math

max_num = 1000000

prime_nums = [
    True 
    for _ in range(max_num+1)
]
prime_nums[0], prime_nums[1] = False, False # 0 and 1 is not prime number 

for i in range(2, int(math.sqrt(max_num)) + 1) :
    if prime_nums[i] : 
        j = 2 
        while i*j <= max_num : 
            prime_nums[i*j] = False 
            j += 1

while 1 :
    n = int(sys.stdin.readline()) # 6 <= n <= 1,000,000
    
    if n == 0 :
        break 

    # 각 케이스에 대해 여러가지 방법이 조재한다면
    # b-a가 가장 큰 것을 출력한다.

    # 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는
    # "Goldbach's conjecture is wrong."을 출력
    
    for i in range(2, (n//2) + 1) :
        if prime_nums[i] and prime_nums[n-i] : 
            print(f'{n} = {i} + {n-i}')
            break 
    