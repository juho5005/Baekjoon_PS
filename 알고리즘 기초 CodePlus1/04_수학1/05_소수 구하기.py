import sys 
m, n = tuple(map(int, sys.stdin.readline().split()))
# 1 <= m,n <= 1,000,000
# 시간 복잡도 고려 필요 

prime_nums = [
    True
    for _ in range(n+1)
]
prime_nums[0], prime_nums[1] = False, False # 0 and 1 is not prime number

# 에라토스테네스의 체 사용
for i in range(2, int((n)**(1/2)) + 1) : 
    if prime_nums[i] : 
        j = 2
        while i*j <= n : 
            prime_nums[i*j] = False 
            j += 1

# m이상 n이하의 소수를 모두 출력하는 프로그램 작성
for elem in range(m, n+1) :
    if prime_nums[elem] : 
        print(elem)
        