# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력
import sys 
n = int(sys.stdin.readline()) # N <= 100
# O(N^4)

nums = list(map(int, sys.stdin.readline().split()))

def is_prime(a) :
    if a == 1 : 
        return False 
    for i in range(2, a) : 
        if a % i == 0 : 
            return False 
    return True 


cnt = 0

for elem in nums :
    if is_prime(elem) :
        cnt += 1
    
print(cnt)
    