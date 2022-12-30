# 자연수 M이상 N이하의 자연수 중 소수를 골라 소수의 합과 최솟값을 찾는 프로그램
import sys 
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
# m, n <= 10,000 
# 2중 for문도 안되는 경우이므로 시간복잡도를 생각해야함 .

def prime_check(n) :
    if n == 1:
        return False 

    for i in range(2, n) :
        if n % i == 0 :
            return False

    return True 

# 최솟값 init 
min_val = 0
try_cnt = 0
prime_cnt =0 

# 전체 합
sum_prime = 0

for i in range(m, n+1) :
    if prime_check(i) :
        if try_cnt == 0 :
            min_val = i 
            try_cnt = float('inf')
        sum_prime += i 
        prime_cnt += 1

if prime_cnt == 0 :
    print(-1)
    sys.exit()


print(sum_prime)
print(min_val)