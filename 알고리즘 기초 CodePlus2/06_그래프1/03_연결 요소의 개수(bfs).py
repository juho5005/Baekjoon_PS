# 연결 요소의 개수 
# N:정점의 개수, M:간선의 개수

# bfs (인접 리스트)

from collections import deque 
import sys 
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
    
    # not specified if it is order by asc, desc 

def bfs() :
    while q :
        curr_v = q.popleft()

        for next_v in graph[curr_v] :
            if not visited[next_v] :
                visited[next_v] = True 
                q.append(next_v)

# initialize
initial()
q = deque()

cnt = 0
for i in range(1, n+1) :
    if not visited[i] :
        cnt += 1
        visited[i] = False 
        q.append(i)
        bfs()

print(cnt)