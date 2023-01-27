# BFS (인접 리스트)
# N : 정점
# M : 간선
# 무방향 그래프

# 정점 번호 : 1 ~ N 
# 모든 간선의 가중치 : 1
# R : 루트 정점 

# BFS 우선 탐색 시 노드의 방문 순서 출력
# 인접 정점은 내림차순 방문

from collections import deque 
import sys 

n, m, r = tuple(map(int, sys.stdin.readline().split()))

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

graph = [
    []
    for _ in range(n+1)
]

visited = [
    0
    for _ in range(n+1)
]

# 방문 순서
cnt = 1


def initial() :
    for s, e in linked_vertex :
        graph[s].append(e)
        graph[e].append(s)
    
    for g in graph  :
        g.sort(reverse=True)


def bfs() :
    global cnt 

    while q : 
        curr_v = q.popleft()
        
        for next_v in graph[curr_v] :
            if visited[next_v] == 0 :
                cnt += 1 
                visited[next_v] = cnt 
                q.append(next_v)

# initialize 
initial()

q = deque()

root_vertex = r 
visited[root_vertex] = cnt 
q.append(root_vertex)

bfs()

# print the results 
for elem in visited[1:] :
    print(elem)