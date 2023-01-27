# 1 : 이동할 수 있는 칸
# 0 : 이동할 수 없는 칸

# (0,0)에서 출발해서 (N-1, M-1) 위치로 이동할 때 지나야 하는 최소의 칸수를 구하시오

from collections import deque 
import sys 
n, m = tuple(map(int, sys.stdin.readline().split())) # 2 <=N,M <= 100
q = deque()

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

elements = [
    sys.stdin.readline().rstrip()
    for _ in range(n)
]

board = []

for i in range(n) :
    board.append([])
    for j in range(m) :
        board[i].append(int(elements[i][j]))

min_dist = [
    [0] * m
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<m 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] :
        return False 
    if board[x][y] == 0 :
        return False 
    return True 

def bfs() :
    while q :
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 

            if can_go(nx, ny) :
                visited[nx][ny] = True 
                q.append((nx, ny))
                min_dist[nx][ny] = min_dist[x][y] + 1

visited[0][0] = True
q.append((0, 0)) 
min_dist[0][0] = 1
bfs()

print(min_dist[n-1][m-1])