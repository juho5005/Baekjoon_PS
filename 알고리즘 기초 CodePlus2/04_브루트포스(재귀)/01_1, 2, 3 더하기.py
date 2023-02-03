# 정수 n이 주어질 때 
# n을 1, 2, 3의 합으로 나타내는 방법의 수는 ?

import sys 
t = int(sys.stdin.readline())

def counting(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    elif n == 3 :
        return 4 
    else :
        return counting(n-1)+counting(n-2)+counting(n-3)

for _ in range(t) :
    n = int(sys.stdin.readline()) # 0 < n < 11
    
    print(counting(n))