# dfs와 bfs로 타맥한 결과를 출력
# 방문할 수 있는 정점이 여러 개 인 경우
# 정점 번호가 작은 것을 먼저 방문하고 
# 더 이상 방문 불가능할 경우 종료

from collections import deque 
import sys 
sys.setrecursionlimit(10**6)
n, m, v = tuple(map(int, sys.stdin.readline().split()))

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

dfs_graph = [
    []
    for _ in range(n+1)
]

dfs_visited = [
    False 
    for _ in range(n+1)
]

bfs_graph = [
    []
    for _ in range(n+1)
]

bfs_visited = [
    False 
    for _ in range(n+1)
]

def dfs_initial() :
    for s, e in linked_vertex : 
        dfs_graph[s].append(e)
        dfs_graph[e].append(s)
    
    # order by asc 
    for dfs_g in dfs_graph :
        dfs_g.sort()

def dfs(vertex) :
    for curr_v in dfs_graph[vertex] :
        if not dfs_visited[curr_v] :
            dfs_visited[curr_v] = True
            dfs_res.append(curr_v) 
            dfs(curr_v)

def bfs_initial() :
    for s, e in linked_vertex : 
        bfs_graph[s].append(e)
        bfs_graph[e].append(s)
    
    # order by asc 
    for bfs_g in bfs_graph :
        bfs_g.sort()

def bfs() :
    while q:
        curr_v = q.popleft()
        
        for next_v in bfs_graph[curr_v] :
            if not bfs_visited[next_v] :
                bfs_visited[next_v] = True 
                bfs_res.append(next_v)
                q.append(next_v)

# dfs
# initialize
dfs_initial()

dfs_res = []

root_vertex = v 
dfs_visited[root_vertex] = True 
dfs_res.append(root_vertex)
dfs(root_vertex)

print(*dfs_res)


# bfs 
bfs_initial()

q = deque()

bfs_res = []

root_vertex = v 
bfs_visited[root_vertex] = True 
bfs_res.append(root_vertex)
q.append(root_vertex)
bfs()

print(*bfs_res)