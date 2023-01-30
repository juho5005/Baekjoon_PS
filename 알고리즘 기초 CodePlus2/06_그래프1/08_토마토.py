# 며칠이 지나면 모든 토마토들이 익는가?
# 최소일수 구하기 -> 최단거리 BFS

from collections import deque 
import sys 

m, n = tuple(map(int, sys.stdin.readline().split()))

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# Declaration of Queue 
q = deque()

# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토 x

visited = [
    [False] * m
    for _ in range(n)
]

dist = [
    [0] * m 
    for _ in range(n)
]

# 상하좌우
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

# bfs
def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<m 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] :
        return False 
    if board[x][y] == -1 :
        return False 
    return True 

def bfs() :
    while q :
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 

            if can_go(nx, ny) :
                visited[nx][ny] = True 
                board[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


# 익어있는 토마토들의 위치 출력
riped_pos = []
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 :
            riped_pos.append((i, j))

# 익은 토마토들의 모든 위치를 q에 삽입
for x, y in riped_pos :
    visited[x][y] = True 
    q.append((x, y))
bfs()
    

# finalize
max_num = float('-inf')
for i in range(n) :
    for j in range(m) :
        if board[i][j] != -1 and not visited[i][j] :
            print(-1)
            sys.exit()
        
        max_num = max(max_num, dist[i][j])

print(max_num)
