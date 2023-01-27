# BFS (인접 리스트)
# N : 정점
# M : 간선
# 무방향 그래프
# 모든 가중치 1
# R : 루트 정점 

# 1 ~ N까지 각 노드의 방문순서를 출력하고
# 방문할 수 없는 경우 0을 출력한다

from collections import deque 
import sys 
n, m, r = tuple(map(int, sys.stdin.readline().split()))

# 양방향, 각 정점의 쌍이 모두 다르다
linked_vertex = [
    list(map(int, sys.stdin.readline().split())) 
    for _ in range(m)
]

# graph 
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
    
    # Cause vertexes visit order by asc, sort by asc 
    for elem in graph :
        elem.sort() # order by asc 

def bfs() :
    global cnt 

    while q : 
        curr_v = q.popleft()
        
        for next_v in graph[curr_v] :
            if visited[next_v] == 0 : # not visited 
                cnt += 1
                visited[next_v] = cnt 
                q.append(next_v)
                

# initialize 
initial()

q = deque()

root_vertex = r 
visited[root_vertex] = 1
q.append(root_vertex)

# implement a function 
bfs()

# print the results 
for elem in visited[1:] :
    print(elem)
