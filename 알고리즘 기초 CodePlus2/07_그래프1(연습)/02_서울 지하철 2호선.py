from collections import deque 
import sys 
sys.setrecursionlimit(10**6)

# the number of station
n = int(sys.stdin.readline()) 

graph = [
    []
    for _ in range(n+1)
]

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# whether cycle 
cycle = False 

visited = [
    False
    for _ in range(n+1)
]

is_cycle = [
    False 
    for _ in range(n+1)
]

dist = [
    -1
    for _ in range(n+1)
]

def initial() :
    for s, e in linked_vertex :
        graph[s].append(e)
        graph[e].append(s)

def dfs(curr_v, start, cnt) :
    global cycle
    
    if cycle :
        return 

    if curr_v == start and cnt >= 2 :
        cycle = True 
        return 
    
    for next_v in graph[curr_v] :
        if not visited[next_v] :
            visited[next_v] = True 
            dfs(next_v, start, cnt+1)
        elif next_v==start and cnt >= 2 :
            dfs(next_v, start, cnt)

# 각 역마다 순환역과 얼마나 떨어져 있는지 확인
def bfs() :
    global dist
    q = deque()

    for i in range(1, n+1) :
        if is_cycle[i] :
            dist[i] = 0
            q.append(i)

    while q :
        curr_v = q.popleft()

        for next_v in graph[curr_v] :
            if dist[next_v] == -1 :
                q.append(next_v) 
                dist[next_v] = dist[curr_v] + 1
    
    for d in dist[1:] :
        print(d, end = ' ')
    return 

# initialize 
initial()

# 모든 역에 대해
for i in range(1, n+1) :
    visited = [
        False
        for _ in range(n+1)
    ]
    cycle = False 
    visited[i] = True 
    dfs(i, i, 0)

    if cycle :
        is_cycle[i] = True 

bfs()