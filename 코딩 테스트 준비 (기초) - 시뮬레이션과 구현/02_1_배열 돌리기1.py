'''
크기가 NxM인 배열이 있을 때 배열을 돌리려고 함
배열은 반시계 방향으로 돌림
'''

import sys 
n, m, r = tuple(map(int, sys.stdin.readline().split()))

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

for _ in range(r) :
    for i in range(min(n, m) // 2) :
        # x, y는 돌려지는 배열 중 가장 첫 번째 배열 인덱스
        x, y = i, i
        temp = board[x][y]

        # 안쪽까지 계속 고려해야하기 때문에 n-i이랑 m-i로 범위 설정
        for j in range(i+1, n-i) : # 좌
            x = j
            prev_value = board[x][y]
            board[x][y] = temp  
            temp = prev_value
        
        for j in range(i+1, m-i) : # 하
            y = j 
            prev_value = board[x][y]
            board[x][y] = temp
            temp = prev_value 
        
        for j in range(i+1, n-i) : # 우
            x = n - j - 1
            prev_value = board[x][y]
            board[x][y] = temp 
            temp = prev_value 
        
        for j in range(i+1, m-i) : # 상
            y = m - j - 1
            prev_value = board[x][y]
            board[x][y] = temp 
            temp = prev_value 

for i in board :
    print(*i)