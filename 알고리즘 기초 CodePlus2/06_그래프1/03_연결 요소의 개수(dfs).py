# 무방향 그래프
# 연결요소의 개수

# N : 정점의 수
# M : 간선의 수 

import sys 
sys.setrecursionlimit(10**6)

n, m = tuple(map(int, sys.stdin.readline().split()))

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

graph = [
    []
    for _ in range(n+1)
]

visited = [
    False 
    for _ in range(n+1)
]

def initial() :
    for s, e in linked_vertex : 
        graph[s].append(e)
        graph[e].append(s)
    
    # order by asc
    for g in graph :
        g.sort()
        

def dfs(vertex) :
    for curr_v in graph[vertex] :
        if not visited[curr_v] :
            visited[curr_v] = True 
            dfs(curr_v)


# intialize 
initial() 

cnt = 0 

for i in range(1, n+1) :
    if not visited[i] :
        visited[i] = True 
        dfs(i)
        cnt += 1

print(cnt)