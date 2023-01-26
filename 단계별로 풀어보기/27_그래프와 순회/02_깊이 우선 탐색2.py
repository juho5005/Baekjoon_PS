# N : 정점
# M : 간선
# 무방향 그래프 
# 가중치 : 1
# R : 루트 정점

# 인접 정점은 내림차순으로 방문

import sys 
sys.setrecursionlimit(10**6)

n, m, r = tuple(map(int, sys.stdin.readline().split()))

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

graph = [
    []
    for _ in range(n+1)
]

for start, end in linked_vertex :
    graph[start].append(end)
    graph[end].append(start)

# 인접 정점은 내림차순으로 방문
for elem in graph  :
    elem.sort(reverse=True)

visited = [
    0
    for _ in range(n+1)
]

cnt = 1

def dfs(vertex) :
    global cnt 

    for curr_v in graph[vertex]  :
        if visited[curr_v] == 0 : # not visited 
            cnt += 1
            visited[curr_v] = cnt 
            dfs(curr_v)

root_vertex = r 
visited[root_vertex] = cnt 

dfs(root_vertex)

for elem in visited[1:] :
    print(elem)