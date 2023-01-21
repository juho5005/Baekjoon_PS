# (N, K) - 요세푸스 순열
from collections import deque 
import sys
n, k = tuple(map(int, sys.stdin.readline().split()))

dq = deque(
    i
    for i in range(1, n+1)
)

print('<', end='')

while len(dq) != 1 :
    for _ in range(k-1) :
        dq.append(dq.popleft())
    
    print(f'{dq.popleft()}, ', end='')
print(f'{dq[0]}', end='')
print('>')