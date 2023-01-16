# 0보다 크거나 같은 정수 N이 주어질 때 
# N!을 출력하는 프로그램 작성

import sys 
n = int(sys.stdin.readline()) # 0 <= N <= 12 

# function of calculating factorial 
def facto(a) :
    if a == 0 : # 0! is 1
        return 1
    return a * facto(a-1)

print(facto(n))