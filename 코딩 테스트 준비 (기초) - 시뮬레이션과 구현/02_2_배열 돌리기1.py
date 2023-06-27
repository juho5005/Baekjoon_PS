# https://velog.io/@leetaekyu2077/%EB%B0%B1%EC%A4%80-16926%EB%B2%88-%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0-1

import sys 
from collections import deque 

n, m, r = tuple(map(int, sys.stdin.readline().split()))

matrix = []
answer = [
    [0] * m
    for _ in range(n)
]
deq = deque()

for i in range(n) :
    matrix.append(list(map(int, sys.stdin.readline().split())))


loops = min(n, m) // 2

for i in range(loops) :
    deq.clear()
    deq.extend(matrix[i][i:m-i]) # 상
    deq.extend([ # 우
        row[m-i-1]
        for row in matrix[i+1:n-i-1]
    ])
    deq.extend(matrix[n-1-i][i:m-i][::-1]) # 하
    deq.extend([ # 좌
        row[i]
        for row in matrix[i+1:n-i-1]
    ][::-1])

    deq.rotate(-r)

    for j in range(i, m-i) : # 상
        answer[i][j] = deq.popleft() 
    
    for j in range(i+1, n-1-i) : # 우
        answer[j][m-i-1] = deq.popleft()
    
    for j in range(m-1-i, i-1, -1) : # 하
        answer[n-i-1][j] = deq.popleft() 
    
    for j in range(n-2-i, i, -1) : # 왼
        answer[j][i] = deq.popleft()

for i in answer :
    print(*i)