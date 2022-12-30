# 9x9, 81개 자연수
# 최댓값이 몇 행 몇 열에 위치하는지 구하시오

import sys 

# 9 x 9 board
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(9)
]

# 최댓값
max_val = max(map(max, board)) # 2차원 배열에서 최댓값 추출
print(max_val)

# check all elements 
for i in range(9) : 
    for j in range(9) :
        if board[i][j] == max_val : 
            print(i+1, j+1)
            print(max_val)
            sys.exit()
    