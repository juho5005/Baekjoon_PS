# 수학 N개를 적고 
# 종이에 적은 수를 M으로 나눴을 때 나머지가 모두 같게 되는 M을 모두 찾으려고 한다. (M >= 1)

# N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성

import sys 
import math 
n = int(sys.stdin.readline()) # 종이에 적은 개수 N (2 <= N <= 100)
# O(N^4)

nums = [
    int(sys.stdin.readline())
    for _ in range(n)
]

nums.sort() # 주어진 수들을 오름차순 정렬
nums_diff = []

for i in range(n-1) : 
    nums_diff.append(nums[i+1] - nums[i])

gcd_num = nums_diff[0]

for i in range(1, n-1) :
    gcd_num = math.gcd(gcd_num, nums_diff[i])

for i in range(2, gcd_num+1) :
    if gcd_num % i == 0 :
        print(i, end = ' ')