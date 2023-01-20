import sys 
n = int(sys.stdin.readline()) # 크기 N 

# 오큰수 
# A(i)의 오큰수는 오른쪽에 있으면서 A(i)보다 큰 수 중에서 가장 왼쪽에 있는 수
# 그러한 수가 없을 경우 -1

nums = list(map(int, sys.stdin.readline().split()))
# 1<= A(i) <= 1,000,000 

ans = [-1] * n 
stack = []

# 인덱스까지 튜플로 묶어서 넣어준다.
stack.append((nums[0],0)) 

for i in range(1, n) :
    
    while stack and stack[-1][0] < nums[i] : 
        idx = stack.pop()[1]
        ans[idx] = nums[i]
    stack.append((nums[i], i))

print(*ans)