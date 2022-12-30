# 1 <= N <= 1,000
# O(N^2)

import sys 
n = int(sys.stdin.readline())

nums = []
for _ in range(n) :
    nums.append(int(sys.stdin.readline()))

# 파이썬의 .sort() 함수는 시간복잡도 : O(N*logN)을 보장해준다.
nums.sort() 

for elem in nums :
    print(elem)