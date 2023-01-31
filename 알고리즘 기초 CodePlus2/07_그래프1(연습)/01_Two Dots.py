# N*M board
# 각각의 칸은 다른 색이 칠해진 공이 존재
# 같은 색으로 이루어진 사이클을 찾는 것

# 사이클(k) 조건
#  >= 4 -> cnt 개수로 4개이상 조건 주면 될듯
# 모든 점의 색은 같음
# 인접하다 -> 상하좌우

# 게임판의 상태가 주어질 때 사이클의 존재 유무 판별

# DFS 사용 -> limit필요

import sys 
sys.setrecursionlimit(10**6)

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

n, m = tuple(map(int, sys.stdin.readline().split()))
# 2<= N,M <= 50

# 2 Dimension
board = [
    [   
        elem
        for elem in sys.stdin.readline().rstrip()
    ]
    for _ in range(n)
]

# whether visited
visited = [
    [False] * m 
    for _ in range(n)
]


# dfs : 2 Dimension
def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y, color) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] : 
        return False 
    if board[x][y] != color :
        return False 
    return True 

def dfs(x, y, color, cnt, s_x, s_y) :
    global cycle
    
    for dx, dy in zip(dxs, dys) :
        nx, ny = x+dx, y+dy 

        if nx==s_x and ny==s_y and cnt >= 4 :
            cycle = True 
            print('Yes')
            sys.exit()

        if can_go(nx, ny, color) :
            visited[nx][ny] = True # lock visit
            
            dfs(nx, ny, color, cnt+1, s_x, s_y) # changed : nx, ny, cnt+1

            visited[nx][ny] = False # lift visit 


# finalize 
cycle = False 

for i in range(n) :
    for j in range(m) :
        s_x, s_y = i, j
        visited[i][j] = True # lock visit

        # (start,end), color(alphabet), cnt, (start, end) 
        dfs(i, j, board[i][j], 1, s_x, s_y)
        
        if cycle : 
            print('Yes')
            sys.exit()

        visited[i][j] = False # lift visit

print('No')