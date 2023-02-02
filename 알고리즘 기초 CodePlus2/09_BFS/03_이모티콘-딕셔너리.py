from collections import deque 
import sys 
s = int(sys.stdin.readline())

# Declaration of Queue
q = deque()

# visited with Dictionary
# add role of dist 
visited = dict()

# initialize 
def bfs() :
    while q :
        x, y = q.popleft()

        if x==s :
            print(visited[(x, y)])
            sys.exit()

        # 1) 화면에 있는 이모티콘을 복사해서 클립보드에 저장 (클립보드의 내용은 덮어쓰기 됨)
        # (x, y) -> (x, x)
        if (x, x) not in visited.keys() :
            visited[(x, x)] = visited[(x, y)] + 1
            q.append((x, x))
        
        # 2) 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 (화면의 이모티콘 + 클립보드의 이모티콘)
        # (x, y) -> (x+y, y)
        if (x+y, y) not in visited.keys() :
            visited[(x+y, y)] = visited[(x, y)] + 1
            q.append((x+y, y))
        
        # 3) 화면에 있는 이모티콘 중 하나 삭제 (클립보드는 삭제 x)
        # (x, y) -> (x-1, y)
        if (x-1, y) not in visited.keys() :
            visited[(x-1, y)] = visited[(x, y)] + 1
            q.append((x-1, y))

# finalize 
# (화면의 이모티콘 개수, 클립보드의 이모티콘 개수)
screen, clipboard = 1, 0
visited[(screen, clipboard)] = 0  
q.append((screen, clipboard))
bfs()