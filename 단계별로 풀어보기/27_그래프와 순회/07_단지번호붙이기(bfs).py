# BFS 
# 1 : 집이 있는 곳 
# 0 : 집이 없는 곳

from collections import deque 
import sys 

n = int(sys.stdin.readline())

q = deque()

elements = [
    sys.stdin.readline().rstrip()
    for _ in range(n)
]

board = []

for i in range(n) :
    board.append([])
    for j in range(n) :
        board[i].append(int(elements[i][j]))

visited = [
    [0] * n
    for _ in range(n)
]

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

cnt = 1

def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if board[x][y] == 0 :
        return False 
    if visited[x][y] != 0 :
        return False 
    return True 

def bfs() :
    global cnt 

    while q :
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 
            
            if can_go(nx, ny) :
                visited[nx][ny] = cnt 
                q.append((nx, ny))

for i in range(n) :
    for j in range(n) :
        if can_go(i, j) :
            visited[i][j] = cnt 
            q.append((i, j))
            bfs()
            cnt += 1

# 단지의 수
complex_cnt = cnt-1
print(complex_cnt)

# 단지의 범위
lst = [
    k
    for k in range(1, complex_cnt+1)
]

res_lst = []

# 각 단지의 집의 개수
for elem in lst :

    res = 0
    for i in range(n) :
        res += visited[i].count(elem)
    res_lst.append(res)

res_lst.sort()

for elem in res_lst :
    print(elem)