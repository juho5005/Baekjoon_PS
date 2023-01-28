# 숨바꼭질 중
# 수빈 : N (0<=N<=100,000)
# 동생 : K (0<=K<=100,000)

# 수빈이는 걷거나 순간이동
# 걷기 : -1 or +1
# 순간이동 : 2 * (자신의 위치)

# 동생의 위치 주어질 때 동생을 찾는 가장 빠른 시간은 몇 초 후 ?
# 최단거리문제 (BFS)

from collections import deque 
import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))

q = deque()

visited = [
    False 
    for _ in range(0, 100001)
]

dist = [
    0
    for _ in range(0, 100001)
]

def bfs() :
    while q :
        curr_v = q.popleft()

        if curr_v == k :
            return dist[curr_v]
        
        for next_v in (curr_v-1, curr_v+1, curr_v*2) :
            if 0 <= next_v <= 100000 and not visited[next_v] :
                visited[next_v] = True 
                q.append(next_v)
                dist[next_v] = dist[curr_v] + 1

visited[n] = True
q.append(n)
print(bfs())