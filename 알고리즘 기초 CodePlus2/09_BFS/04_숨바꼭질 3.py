# 수빈 : N 
# 동생 : K
# 0 <= N,K <= 100,000
INT_MAX = 100000

# 걷기 -> 1초후에 x-1, x+1 
# 순간이동 -> 0초후에 2*x
# 동생을 찾는 가장 빠른 시간구하기 -> 최단거리 : BFS
from collections import deque 
import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))

# Declaration of Queue 
q = deque()

visited = [
    False
    for _ in range(INT_MAX+1)
]

dist = [
    0
    for _ in range(INT_MAX+1)
]

def bfs() :
    while q :
        curr_v = q.popleft()

        if curr_v == k :
            return dist[curr_v]

        for next_v in (curr_v-1, curr_v+1, curr_v*2) :
            if 0<=next_v<=INT_MAX and not visited[next_v] :
                if next_v == curr_v*2 :
                    visited[next_v] = True 
                    q.appendleft(next_v) 
                    dist[next_v] = dist[curr_v] 
                else :
                    visited[next_v] = True 
                    q.append(next_v)
                    dist[next_v] = dist[curr_v] + 1

visited[n] = True 
q.append(n)
print(bfs())