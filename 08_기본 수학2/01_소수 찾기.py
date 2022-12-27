import sys 
n = int(sys.stdin.readline()) # n <= 100
# O(N^4) : 4중 for문 허용

nums = list(map(int, sys.stdin.readline().split())) # 1<= nums <= 1000

def prime_check(n) :
    if n == 1:
        return False 

    checking = True 
    for i in range(2, n) :
        if n % i == 0 :
            checking = False
            break 
    
    return checking

cnt = 0 
for num in nums : 
    if prime_check(num) :
        cnt += 1

print(cnt)