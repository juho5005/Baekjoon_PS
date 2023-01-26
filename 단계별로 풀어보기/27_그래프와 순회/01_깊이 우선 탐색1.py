# 인접 행렬을 사용하면 메모리 초과로 인해 풀 수 없다.
# 인접 리스트를 사용하기
# dfs에선 sys.setrecursion(10**6)을 뺴먹지 말기

import sys 
sys.setrecursionlimit(10**6)
# n : 정점의 수
# m : 간선의 수 
# r : 시작 정점

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

# 그래프 정렬
for i in range(n+1) :
    graph[i].sort()

visited = [
    0
    for _ in range(n+1)
]

# 순차를 나타낼 cnt 변수
cnt = 1

def dfs(vertex) : 
    global cnt 

    for curr_v in graph[vertex] :
        if visited[curr_v] == 0 :
            cnt += 1
            visited[curr_v] = cnt
            dfs(curr_v) 

root_vertex = r 
visited[r] = cnt 

dfs(root_vertex)


for i in range(1, n+1) :
    print(visited[i])