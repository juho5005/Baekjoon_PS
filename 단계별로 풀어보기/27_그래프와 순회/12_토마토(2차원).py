# m x n의 상자
# 인접한 곳 : 상하좌우
# 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지
# 그 최소일수를 알고싶다.

# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 들어있지 않음

# 토마토가 모두 익을 때까지의 최소 날짜를 출력
# 단, 저장될때부터 모든 토마토가 익어있는 경우는 0출력
# 단, 토마토가 모두 익지 못하는 상황에선 -1출력 

from collections import deque 
import sys 
m, n = tuple(map(int, sys.stdin.readline().split())) # 상자의 크기 (m x n), O(N^3) 

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# idea
# 어느 지점에서 시작해야 될지 모르는 상황! 
# 모든 지점에서 경우를 따져봐서 
# 모든 경우를 따져봐도 토마토가 다 익는 경우가 없다면 -1출력하고
# 모든 토마토가 익는 날짜를 리스트에 넣어서 min 씌우면 해결가능할 것 같다.
# 최단거리를 구해야 하므로 BFS 사용 결정 


# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# bfs~
def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<m 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if board[x][y] == -1 :
        return False 
    if visited[x][y] :
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


# riped tomato points
riped_points = []

# 토마토가 익은 1인 모든 지점을 추출
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 :
            riped_points.append((i, j))

# Declaration of Queue 
q = deque()
        
# check visit
visited = [
    [False] * m
    for _ in range(n)
]
        
# consuming time
dist = [
    [0] * m
    for _ in range(n)
]

for l in range(len(riped_points)) :
    visited[riped_points[l][0]][riped_points[l][1]] = True 
    q.append((riped_points[l][0], riped_points[l][1]))

# Implementation of bfs 
bfs()

# 토마토가 모두 익는 경우가 없을 경우
for i in range(n) :
    for j in range(m) :
        if not visited[i][j] and board[i][j] != -1 :
            print(-1)
            sys.exit()

print(max(map(max, dist)))