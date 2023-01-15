# 양의 정수 n이 주어졌을 때
# 가능한 모든 쌍의 GCD의 합을 구하는 프로그램 작성

import sys 
from itertools import combinations
t = int(sys.stdin.readline()) # O(N^4)

# 최대공약수 (the greatest common divisor)
def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b 
    return a 

for _ in range(t) :
    cases = list(map(int, sys.stdin.readline().split()))
    cases.remove(cases[0])
    
    res = 0

    for elem in combinations(cases, 2) :
        res += gcd(elem[0], elem[1])
        
    print(res)
