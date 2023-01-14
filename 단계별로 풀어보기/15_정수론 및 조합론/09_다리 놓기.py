# 서쪽 : N
# 동쪽 : M 
# N <= M (즉, 동쪽의 다리수가 서쪽의 다리수 보다 많거나 같음)

import sys
import math  
t = int(sys.stdin.readline())

for _ in range(t) :
    n, m = tuple(map(int, sys.stdin.readline().split()))
    print(math.comb(m, n))