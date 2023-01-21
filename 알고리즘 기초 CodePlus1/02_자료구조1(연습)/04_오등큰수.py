# 오등큰수
# 크기가 N인 수열 A(1) ~ A(N)
# 오등큰수란 A(i)보다 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중
# 가장 왼쪽에 있는 수를 의미한다.
# 오등큰수가 없는 경우 -1이다.

import sys 
n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

# 각 원소의 개수를 딕셔너리에 삽입
dic = {}
for elem in nums :
    if elem not in dic :
        dic[elem] = 1
    else :
        dic[elem] += 1

ans = [-1] * n

stack = []
# (주어진 수의 개수, 인덱스) 삽입
stack.append((dic[nums[0]], 0)) 

for i in range(1, n) :
    while stack and stack[-1][0] < dic[nums[i]] :
        ans[stack.pop()[1]] = nums[i]
    
    stack.append((dic[nums[i]], i))

print(*ans)