import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))
# 1 <= n <= 10 <= k <= n 

# (n, k)를 출력하시오 

def factorial(num) :
    result = 1
    while num >= 1 :
        result *= num
        num -= 1
    return result 

print(factorial(n)//(factorial(n-k)*factorial(k)))
