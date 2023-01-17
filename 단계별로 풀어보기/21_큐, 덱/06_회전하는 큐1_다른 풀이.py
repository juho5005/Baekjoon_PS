from collections import deque 
import sys 

# 큐의 크기 : N, 뽑아내려고 하는 수의 개수 M
# 1 <= N <= 50, M <= N 
n, m = tuple(map(int, sys.stdin.readline().split()))

# 뽑아내려고 하는 각각의 수들의 위치
posi = list(map(int, sys.stdin.readline().split()))

# 큐 생성
dq = deque(
    i
    for i in range(1, n+1) 
)

# 총 연산의 횟수
cnt = 0

for p in posi :
    # 원하는 값을 발견했을 때 
    if dq[0] == p :
        dq.popleft()
        continue
    
    # 왼쪽으로 이동하는 것이 이득일 때
    if dq.index(p) <= len(dq)//2 :
        while dq[0] != p :
            dq.append(dq.popleft())
            cnt += 1
        dq.popleft()
    
    else : 
        while dq[0] != p :
            dq.appendleft(dq.pop())
            cnt += 1
        dq.popleft()

print(cnt)