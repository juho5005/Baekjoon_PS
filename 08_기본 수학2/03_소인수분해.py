# 정수 N이 주어질 때, 소인수분해 하시오 
import sys 
n = int(sys.stdin.readline()) 
# 1 <= N <= 10,000,000
# 되도록 O(1)을 목표로 코드 구성하기 

if n == 1 :
    sys.exit()

# 비교 시작점
s = 2

while n != 1 :
    if n % s == 0 : 
        print(s) 
        n //= s 
    else :
        s += 1 
