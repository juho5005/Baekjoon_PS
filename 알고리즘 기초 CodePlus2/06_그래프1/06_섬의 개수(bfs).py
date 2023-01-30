# 섬과 바다 지도가 주어질 때
# 섬의 개수 구하기

# 같은 섬에 있다는 것은
# 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있는 것

# 1 : 땅
# 0 : 바다

# bfs 

from collections import deque 
import sys 

# direction (상하좌우, 대각선)
dxs = [1, 1, 1, 0, 0, -1, -1, -1]
dys = [1, 0, -1, -1, 1, 1, 0, -1]



while 1 :
    w, h = tuple(map(int, sys.stdin.readline().split()))
    q= deque()
    # 1<= w,h <= 50

    # terminate condition
    if w == 0 and h == 0 :
        sys.exit() 

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

    def bfs() :
        while q :
            x, y = q.popleft()

            for dx, dy in zip(dxs, dys) :
                nx, ny = x+dx, y+dy 

                if can_go(nx, ny) :
                    visited[nx][ny] = True 
                    q.append((nx, ny))
    
    # initialize the number of land
    land_cnt = 0

    board = [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(h)
    ]

    # collect the data of land 
    land_lst = []

    for i in range(h) :
        for j in range(w) :
            if board[i][j] == 1 : 
                land_lst.append([i,j])

    visited = [
        [False] * w 
        for _ in range(h)
    ]

    
    # finalize 
    for x, y in land_lst :
        if not visited[x][y] :
            visited[x][y] = True 
            q.append((x, y))
            bfs() 
            land_cnt += 1
    
    print(land_cnt)