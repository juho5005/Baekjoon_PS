# 미로 : N*M -> 벽 or 빈 방
# 빈 방은 자유롭게 다니지만, 벽은 부수지 않으면 이동 불가

# 무기를 사용해 벽을 부수면 빈 방과 동일한 방으로 변해서 이동 가능
# (1, 1)에서 (N, M)으로 이동하려면 벽을 "최소" 몇 개 부셔야 하는가?

# 최소거리 구하는 문제이므로 BFS
# 0으로 이동할 땐 비용 0 -> appendleft
# 1으로 이동할 땐 비용 1 -> append 
# 0-1 BFS 

from collections import deque 
import sys 
# Declaration of Queue
q = deque()

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 0 : 빈 방
# 1 : 벽

m, n = tuple(map(int, sys.stdin.readline().split()))

# board
board = [
    [
        int(elem)
        for elem in sys.stdin.readline().rstrip()
    ]
    for _ in range(n)
]

# visited
visited = [
    [False] * m
    for _ in range(n)
]

# dist 
dist = [
    [0] * (m)
    for _ in range(n)
]

# bfs 
def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<m 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] :
        return False 
    # 0과 1모두 이동 가능함
    return True 

def bfs() :
    while q :
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 

            if can_go(nx, ny) :
                
                # 벽이 없는 경우
                if board[nx][ny] == 0 : 
                    dist[nx][ny] = dist[x][y] # 벽을 깬 횟수 그대로
                    visited[nx][ny] = True
                    q.appendleft((nx, ny)) # 벽이 없는 곳을 우선적으로 돌도록 큐의 왼쪽에 삽입
                
                # 벽이 있는 경우
                elif board[nx][ny] == 1 :
                    dist[nx][ny] = dist[x][y] + 1 # 여태까지 벽을 깬 횟수 + 1
                    visited[nx][ny] = True 
                    q.append((nx, ny)) # 벽이 있는 곳을 나중에 돌도록 큐의 오른쪽에 삽입


# (0, 0)에서 시작해서 (N-1, M-1)으로 이동
visited[0][0] = True 
q.append((0, 0))
bfs()

# 총 소요된 거리 출력
print(dist[-1][-1]) # =(dist[n-1][m-1])