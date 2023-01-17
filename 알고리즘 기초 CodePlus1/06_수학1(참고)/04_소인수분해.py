# 정수 N이 주어졌을 때, 소인수분해 하는 프로그램 작성

import sys 
n = int(sys.stdin.readline())
# 1<= N <= 10,000,000 
# 시간복잡도 고려 대상 

if n==1 : 
    sys.exit()

start = 2 
while n != 1 : 
    if n % start == 0 : 
        n //= start 
        print(start)
    else :
        start += 1
