# 두 자연수 A와 B가 주어졌을 때 A와 B의 최소공배수를 구하는 프로그램 작성.

import sys 
t = int(sys.stdin.readline()) # 1 <= T <= 1000
# O(N^2)

def gcd(a, b) :
    while b > 0 : 
        a, b = b, a%b 
    return a 

def lcm(a, b) :
    return a * b // gcd(a, b)

for _ in range(t) :
    a, b = tuple(map(int, sys.stdin.readline().split()))
    print(lcm(a, b))