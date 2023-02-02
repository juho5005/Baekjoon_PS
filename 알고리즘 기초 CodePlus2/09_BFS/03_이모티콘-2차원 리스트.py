from collections import deque 
import sys 
s = int(sys.stdin.readline())

# Declaration of Queue
q = deque()

# Maximum num
INT_MAX = 1000

# whether visited
visited = [
    [False] * (INT_MAX+1)
    for _ in range(INT_MAX+1)
]

# dist 
dist = [
    [0] * (INT_MAX+1)
    for _ in range(INT_MAX+1)
]

# initialize 
def in_range(x, y) :
    return x>=0 and x<=INT_MAX and y>=0 and y<=INT_MAX 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] :
        return False 
    return True 

def bfs() :
    # x : screen
    # y : clipboard
    while q :
        x, y = q.popleft()

        # terminate condition
        if x == s :
            print(dist[x][y])
            sys.exit()

        # 1) 화면에 있는 이모티콘을 복사해서 클립보드에 저장 (클립보드의 내용은 덮어쓰기 됨)
        # (x, y) -> (x, x)
        if can_go(x, x) :
            visited[x][x] = True 
            q.append((x, x))
            dist[x][x] = dist[x][y] + 1
        
        # 2) 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 (화면의 이모티콘 + 클립보드의 이모티콘)
        # (x, y) -> (x+y, y)
        if can_go(x+y, y) :
            visited[x+y][y] = True 
            q.append((x+y, y))
            dist[x+y][y] = dist[x][y] + 1
        

        # 3) 화면에 있는 이모티콘 중 하나 삭제 (클립보드는 삭제 x)
        # (x, y) -> (x-1, y)
        if can_go(x-1, y) :
            visited[x-1][y] = True 
            q.append((x-1, y))
            dist[x-1][y] = dist[x][y] + 1

# finalize 
screen, clipboard = 1, 0 
visited[screen][clipboard] = True 
q.append((screen, clipboard))
bfs() 