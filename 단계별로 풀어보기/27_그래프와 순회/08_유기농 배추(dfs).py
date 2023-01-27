# 상하좌우 네 방향에 다른 배추가 위치한 경우
# 서로 인접해있다고 본다

# 서로 인접해 있는 배추들이 몇 군데에 퍼져있는지 조사하면
# 총 몇마리의 지렁이가 필요한지 알 수 있다.

# 0 : 배추 x
# 1 : 배추 o

# 필요한 최소의 배추흰지렁이 마리 수를 출력

# dfs 

import sys 
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(t) :
    # n : 가로
    # m : 세로
    # k : 배추가 심어져 있는 위치의 개수
    n, m, k = tuple(map(int, sys.stdin.readline().split()))

    linked_vertex = [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(k)
    ]

    graph = [
        [0] * (m+1)
        for _ in range(n+1)
    ]

    for row, col in linked_vertex :
        graph[row][col] = 1

    visited = [
        [0] * (m+1)
        for _ in range(n)
    ]

    cnt = 1

    def in_range(x, y) :
        return x>=0 and x<n and y>=0 and y<m 

    def can_go(x, y) :
        if not in_range(x, y) :
            return False 
        if visited[x][y] != 0 :
            return False 
        if graph[x][y] == 0 : 
            return False 
        return True 
    
    def dfs(x, y) :
        global cnt 
        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 

            if can_go(nx, ny) :
                visited[nx][ny] = cnt 
                dfs(nx, ny)
    
    for i in range(n) :
        for j in range(m) :
            if can_go(i, j) :
                visited[i][j] = cnt 
                dfs(i, j)
                cnt += 1
    
    print(cnt-1)