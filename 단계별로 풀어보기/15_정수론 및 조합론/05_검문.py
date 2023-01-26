# 숫자 N개를 종이에 적고
# 종이에 적은 수들을 M으로 나눌 때
# 나머지가 모두 같게 되는 M을 모두 찾으려고 함
# 단, M은 1보다 커야함

# N이 주어질 때 가능한 M을 모두 찾는 프로그램 작성

import sys 
import math 
n = int(sys.stdin.readline()) # 2 <= N <= 100 
# O(N^4) 

nums = [
    int(sys.stdin.readline())
    for _ in range(n)
] # 1 <= num <= 1,000,000,000, not duplicated 

# variable 'm' is always exists 

# 최대공약수 함수 
def gcd(a, b) :
    while b > 0 :
        a, b = b, a%b
    return a 

# n개의 숫자들의 각각의 차를 n-1개 구해서 그 수들의 최대공약수를 구해주면 된다.
diff = []

for i in range(1, n) :
    diff.append(abs(nums[i]-nums[i-1])) # abs is applied 

common_gcd = diff[0]

for j in range(1, n-1) :
    common_gcd = gcd(common_gcd, diff[j])

# 약수를 효율적으로 구하는 방식
ans = []
for k in range(1, int(math.sqrt(common_gcd))+1) :
    if common_gcd % k == 0 :
        ans.append(k)
        if k != common_gcd//k : 
            ans.append(common_gcd//k)

# 오름차순 정렬
ans.sort()

# 문제에서 약수에서 1을 제거하라 했으므로 1을 제거
ans.remove(1)

print(*ans)