import sys
t = int(sys.stdin.readline())

board = [
    [0] * 101
    for _ in range(101)
]

for _ in range(t) :
    x, y = tuple(map(int, sys.stdin.readline().split()))
    
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            board[i][j] = 1

area = 0

for k in range(1, 101) :
    for l in range(1, 101) :
        if board[k][l] == 1 :
            area += 1

print(area)

