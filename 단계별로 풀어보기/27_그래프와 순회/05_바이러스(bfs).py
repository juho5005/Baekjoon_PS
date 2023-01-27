# 1번 컴퓨가 바이러스에 걸렸을 때
# 컴퓨터의 수와 네트워크 상에서 연결되어 있는 정보가 주어짐

# 이 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력

# bfs (인접 리스트)

from collections import deque 
import sys 
n = int(sys.stdin.readline()) # the number of computer  # n <= 100 
# O(N^4)

m = int(sys.stdin.readline()) # the number of linked line

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
    
    # 정점을 오름차순, 내림차순 순으로 방문한다는 이야기가 없으므로 정렬할 필요는 없다.

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

root_vertex = 1
visited[root_vertex] = True 
q.append(root_vertex)

bfs()

virus_cnt = 0

for i in range(1, n+1) :
    if visited[i] :
        virus_cnt += 1

print(virus_cnt-1)