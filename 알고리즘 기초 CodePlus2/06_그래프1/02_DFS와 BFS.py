# DFS / BFS
# 오름차순으로 방문
# 더 이상 방문할 수 있는 점이 없는 경우 종료
# 정점번호는 1~N번

from collections import deque 
import sys 
sys.setrecursionlimit(10**6)

n, m, v = tuple(map(int, sys.stdin.readline().split()))

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m) 
]

# Declaration of queue 
q = deque()

dfs_graph = [
    []
    for _ in range(n+1)
]

bfs_graph = [
    []
    for _ in range(n+1)
]

dfs_visited = [
    False 
    for _ in range(n+1)
]

bfs_visited = [
    False 
    for _ in range(n+1)
]

def dfs_initial() :
    # input s, e
    for s, e in linked_vertex :
        dfs_graph[s].append(e)
        dfs_graph[e].append(s)
    
    # sort the graph
    for g in dfs_graph :
        g.sort()

def bfs_initial() :
    # input s, e
    for s, e in linked_vertex : 
        bfs_graph[s].append(e)
        bfs_graph[e].append(s)
    
    # sort the graph 
    for g in bfs_graph :
        g.sort()

def dfs(curr_v) :
    for next_v in dfs_graph[curr_v] :
        if not dfs_visited[next_v] :
            dfs_visited[next_v] = True 
            print(next_v, end =' ')
            dfs(next_v)

def bfs() :
    while q :
        curr_v = q.popleft()

        for next_v in bfs_graph[curr_v] :
            if not bfs_visited[next_v] :
                bfs_visited[next_v] = True 
                print(next_v, end = ' ')
                q.append(next_v)


# initialize dfs
dfs_initial()
root_vertex = v 

dfs_visited[root_vertex] = True 
print(root_vertex, end= ' ')
dfs(root_vertex)
print()

# initialize bfs
bfs_initial()
root_vertex = v 

bfs_visited[root_vertex] = True 
print(root_vertex, end = ' ')
q.append(root_vertex)
bfs()