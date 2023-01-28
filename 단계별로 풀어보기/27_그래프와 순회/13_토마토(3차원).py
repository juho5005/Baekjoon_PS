from collections import deque 
import sys 
m, n, h = tuple(map(int, sys.stdin.readline().split()))

# 큐 선언
q = deque()

# n : 세로, m : 가로, h : 높이
# 3차원 판 생
board = [
    [list(map(int, sys.stdin.readline().split()))
        for _ in range(n)
    ]
    for _ in range(h)
]

visited = [
    [
        [False] * m
        for _ in range(n)
    ]
    for _ in range(h)
]

dist = [
    [
        [0] * m
        for _ in range(n)
    ]
    for _ in range(h)
]

# 익은 토마토의 이동방향 (6)
# 아래, 위, 오른쪽, 왼쪽, 위, 아래
dxs = [1, -1, 0, 0, 0, 0]
dys = [0, 0 ,1, -1, 0, 0]
dzs = [0, 0, 0, 0, 1, -1]

def in_range(x, y, z) :
    return x>=0 and x<h and y>=0 and y<n and z>=0 and z<m

def can_go(x, y, z) :
    if not in_range(x, y, z) :
        return False 
    if visited[x][y][z] :
        return False 
    if board[x][y][z] == -1 :
        return False 
    return True 

def bfs() :
    while q :
        x, y, z = q.popleft()

        for dx, dy, dz in zip(dxs, dys, dzs) :
            nx, ny, nz = x+dx, y+dy, z+dz 

            if can_go(nx, ny, nz) :
                visited[nx][ny][nz] = True 
                q.append((nx, ny, nz))
                dist[nx][ny][nz] = dist[x][y][z] + 1


riped_tomatos = []
# 익은 토마토들의 위치를 추출
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if board[i][j][k] == 1 :
                riped_tomatos.append((i, j, k))

# 좌표 (높이, 세로, 가로) : 인덱싱 0부터 시
# 익은 토마토들의 좌표를 q에 append

for elem in riped_tomatos :
    visited[elem[0]][elem[1]][elem[2]] = True 
    q.append((elem[0], elem[1], elem[2]))

# bfs 실행
bfs()

# 모든 토마토가 익는 경우가 존재하지 않는 경우
ans = float('-inf')
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if not visited[i][j][k] and board[i][j][k] != -1 :
                print(-1)
                sys.exit()
            ans = max(ans, dist[i][j][k])
# 최단거리 출력
print(ans)