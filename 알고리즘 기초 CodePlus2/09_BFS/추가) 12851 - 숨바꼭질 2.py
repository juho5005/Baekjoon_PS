from collections import deque 
import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))
INT_MAX = 100000

# Declaration of Queue
q = deque()

# visited 
visited = [
    False 
    for _ in range(INT_MAX+1)
]

# dist 
dist = [
    0
    for _ in range(INT_MAX+1)
]

# 최단거리로 가는 경우의 가짓수
# cnt 
cnt = 0

# function of bfs 
def bfs() :
    global cnt 

    while q: 
        curr_v = q.popleft()

        if curr_v == k :
            cnt += 1
            continue 
        
        for next_v in (curr_v-1, curr_v+1, curr_v*2) :
            if 0 <= next_v <= INT_MAX :
                if not visited[next_v] or dist[next_v] == dist[curr_v] + 1 :
                    visited[next_v] = True 
                    dist[next_v] = dist[curr_v] + 1
                    q.append(next_v)


# finalize (visited, q.append) 
visited[n] = True 
q.append(n) 

# implement bfs
bfs()

# print minimum dist, cnt
print(dist[k])
print(cnt)