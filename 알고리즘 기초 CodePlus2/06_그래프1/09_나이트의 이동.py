from collections import deque 
import sys 
t = int(sys.stdin.readline())

# direction
dxs = [1, 2, 2, 1, -1, -2, -2, -1]
dys = [2, 1, -1, -2, 2, 1, -1, -2]

for _ in range(t) :
    n = int(sys.stdin.readline()) # 4<=n<=300

    # start : (a, b)
    # end : (c, d)

    a, b = tuple(map(int, sys.stdin.readline().split()))
    c, d = tuple(map(int, sys.stdin.readline().split()))

    # declaration of queue 
    q = deque()

    visited = [
        [False] * n
        for _ in range(n)
    ]

    dist = [
        [0] * n
        for _ in range(n)
    ]

    # bfs
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

            if x==c and y==d :
                return dist[c][d]

            for dx, dy in zip(dxs, dys) :
                nx, ny = x+dx, y+dy

                if can_go(nx, ny) :
                    visited[nx][ny] = True 
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    

    # start
    visited[a][b] = True 
    q.append((a, b))
    print(bfs())