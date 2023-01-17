# N장의 카드 
# 1 ~ N까지의 번호 

# 제일 위에 있는 카드를 바닥에 버리고 
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

# N이 주어질 때 
# 제일 마지막에 남게되는 카드를 구하시오

import sys 
from collections import deque 

n = int(sys.stdin.readline()) 
# 1 <= N <= 500,000 

# delcaration deque 
dq = deque(
    i
    for i in range(1, n+1)
)

while 1 : 
    if len(dq) == 1 : 
        print(dq[0])
        break 

    dq.popleft()
    dq.append(dq.popleft())
