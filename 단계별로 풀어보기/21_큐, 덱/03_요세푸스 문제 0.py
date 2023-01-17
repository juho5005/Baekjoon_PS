# 1번 ~ N번까지 
# N명의 사람이 원을 이루며 앉아있고

# 양의정수 K(<=N)이 주어질 때
# 순서대로 K번째 사람을 제거 

from collections import deque 
import sys 

n, k = tuple(map(int, sys.stdin.readline().split()))

dq = deque(
    i
    for i in range(1, n+1)  
)
print('<', end='')

while 1 : 
    if len(dq) == 1 :
        print(dq[0], end ='')
        break 

    for _ in range(k-1) :
        dq.append(dq.popleft())
    print(dq.popleft(), end =', ')

print('>')