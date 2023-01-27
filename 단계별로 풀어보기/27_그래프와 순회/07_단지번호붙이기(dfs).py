# 1 : 집이 있는 곳
# 0 : 집이 없는 곳

# 집의 모임인 단지를 정의하고 단지에 정의를 붙이려고 함
# 단, 대각선은 연결된 것이 아니다

# dfs 

import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

elements = [
    sys.stdin.readline().rstrip()
    for _ in range(n)
]

board = []

for i in range(n) :
    board.append([])
    for j in range(n) :
        board[i].append(int(elements[i][j]))


visited = [
    [0] * n
    for _ in range(n)
]

# 단지의 수 
cnt = 1

def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<n 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] != 0 :
        return False 
    if board[x][y] == 0 :
        return False 
    return True 

def dfs(x, y) :
    global cnt 

    # 상하좌우
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys) :
        nx, ny = x+dx, y+dy 

        if can_go(nx, ny) :
            visited[nx][ny] = cnt 
            dfs(nx, ny)


for i in range(n) :
    for j in range(n) :
        if can_go(i, j) :
            visited[i][j] = cnt 
            dfs(i, j)
            cnt += 1

# 단지의 수 
complex_num = cnt - 1
print(complex_num)

lst = [
    k
    for k in range(1, complex_num+1)
]

res_lst = []
# 각 단지의 집의 개수 
for elem in lst :
    
    res =0 

    for i in range(n) :
        res += visited[i].count(elem)  
    res_lst.append(res)

res_lst.sort()

for elem in res_lst : 
    print(elem)