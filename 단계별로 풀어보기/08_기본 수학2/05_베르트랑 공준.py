# 베르트랑 공준
# 임의의 자연수 n에 대하여 n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재
# 즉,  // "n초과" ~ "2n이하" // 안에는 적어도 한 개의 소수 존재

import sys 
import math

# n의 최대를 구한다.
max_n = 123456

eratos = [
    True
    for _ in range((2*max_n) + 1)
]
eratos[0], eratos[1] = False, False # 0, 1 is not a prime number

# 에라토스테네스의 체 
for i in range(2, int(math.sqrt(2*max_n)) + 1) :
    if eratos[i] : 
        j = 2 
        while i * j <= 2*max_n : 
            eratos[i*j] = False 
            j += 1 
    
while 1 :
    n = int(sys.stdin.readline()) # 임의의 자연수 n 입력
    
    if n == 0 :
        break # terminate 

    cnt = 0 
    for i in range(n+1, (2*n)+1) :
        if eratos[i] :
            cnt += 1
    
    print(cnt)