# 피보나치 수
# 0과 1로 시작, 0번째 피보나치 수 = 0, 1번째 피보나치 수 = 1
# 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램 작성

import sys 
n = int(sys.stdin.readline())
# 0 <= n <= 20

pibo = [0, 1]

start = 2

def pibo_func(n) :
    global start 

    pibo.append(pibo[start-1] + pibo[start-2])

    if start == n : 
        return pibo[start]

    start += 1
    return pibo_func(n)

if n == 0 or n == 1 :
    print(pibo[n])
else :
    print(pibo_func(n))