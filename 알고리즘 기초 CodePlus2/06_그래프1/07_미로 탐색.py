# 미로 탐색

# 1 : 이동가능한 칸
# 0 : 이동할 수 없는 칸

# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
# 지나야 하는 최소의 칸 수 

# bfs
# 시작점을 (0, 0)으로 설정
# 끝점을 (n-1, m-1)으로 설정 

from collections import deque 
import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

elements = [
    sys.stdin.readline().rstrip()
    for _ in range(n)
]

board = []
for i in range(n) :
    board.append([])
    for j in range(m) :
        board[i].append(int(elements[i][j]))

visited = [
    [False] * m
    for _ in range(n)
]

# dist 
dist = [
    [0] * m
    for _ in range(n)
]

# delcaration of queue 
q = deque()

# direction
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
                dist[nx][ny] = dist[x][y] + 1


# start point
visited[0][0] = True 
q.append((0, 0))
# include start's point 
dist[0][0] = 1
bfs()

# finalize 
print(dist[-1][-1])