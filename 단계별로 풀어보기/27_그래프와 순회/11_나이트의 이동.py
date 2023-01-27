from collections import deque 
import sys
t = int(sys.stdin.readline()) # the number of test_case 

# 나이트의 이동 경로
dxs = [1, 2, 2, 1, -1, -2, -2, -1]
dys = [2, 1, -1, -2, 2, 1, -1, -2]

def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<n 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] :
        return False 
    return True 

def bfs() :
    while q :
        x, y = q.popleft()

        if x == next_x and y == next_y :
            return dist[x][y] 
        
        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 

            if can_go(nx, ny) :
                visited[nx][ny] = True 
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

for _ in range(t) :
    n = int(sys.stdin.readline()) # 4 <= n <= 300

    curr_x, curr_y = tuple(map(int, sys.stdin.readline().split()))
    next_x, next_y = tuple(map(int, sys.stdin.readline().split()))

    # declaration of Queue 
    q = deque()

    visited = [
        [False] * n
        for _ in range(n)
    ]
    
    dist = [
        [0] * n
        for _ in range(n)
    ]
    
    # start
    visited[curr_x][curr_y] = True 
    q.append((curr_x, curr_y))
    print(bfs())