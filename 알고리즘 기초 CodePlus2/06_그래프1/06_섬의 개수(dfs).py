# 섬과 바다 지도가 주어질 때
# 섬의 개수 구하기

# 같은 섬에 있다는 것은
# 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있는 것

# 1 : 땅
# 0 : 바다

# dfs

import sys 
sys.setrecursionlimit(10**6)

# direction (상하좌우, 대각선)
dxs = [1, 1, 1, 0, 0, -1, -1, -1]
dys = [1, 0, -1, -1, 1, 1, 0, -1]

# 1 : 땅
# 0 : 바다 

while 1 :
    w, h = tuple(map(int, sys.stdin.readline().split()))

    if w == 0 and h == 0 :
        sys.exit()


    board = [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(h)
    ]

    visited = [
        [False] * w
        for _ in range(h)
    ]

    # collect land coordinates
    land_lst = []
    for i in range(h) :
        for j in range(w) :
            if board[i][j] == 1 :
                land_lst.append((i, j))
    
    def in_range(x, y) :
        return x>=0 and x<h and y>=0 and y<w 

    def can_go(x, y) :
        if not in_range(x, y) :
            return False 
        if visited[x][y] : 
            return False 
        if board[x][y] == 0 :
            return False 
        return True 

    def dfs(x, y) :
        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 

            if can_go(nx, ny) :
                visited[nx][ny] = True 
                dfs(nx, ny)

    land_cnt = 0

    for x, y in land_lst :
        if not visited[x][y] :
            visited[x][y] = True 
            dfs(x, y)
            land_cnt += 1

    print(land_cnt)
