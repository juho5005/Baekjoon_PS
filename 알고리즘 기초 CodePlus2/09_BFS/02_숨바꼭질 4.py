# 수빈 위치 : N -> O(1), O(logN), O(N), O(NlogN)
# 동생 위치 : K -> ''

# 수빈의 위치가 x일 때
# 이동가능 : x-1, x+1, 2*x

# 수빈이가 동생을 찾는 가장 빠른 시간 구하기
# 최단거리 찾는 문제 -> BFS 

from collections import deque 
import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))

INT_MAX = 100000

visited = [
    False 
    for _ in range(INT_MAX+1)
]

dist = [
    0
    for _ in range(INT_MAX+1)
]

# move[next_v] (현재 노드) = curr_v (부모 노드)
# move 배열에는 이전에 어떤 노드를 지나왔는지 기록되어 있으므로 
# 그 경로를 탐색해서 배열에 넣고 거꾸로 출력
move = [
    0
    for _ in range(INT_MAX+1)
]

# Declaration of Queue 
q = deque()

def path(curr_v) :
    process = []

    tmp = curr_v
    for i in range(dist[curr_v]+1) :
        process.append(tmp)
        tmp = move[tmp]
    print(*process[::-1])

def bfs() :
    while q :
        curr_v = q.popleft()

        if curr_v == k :
            return curr_v

        for next_v in (curr_v-1, curr_v+1, curr_v*2) :
            if 0<=next_v<=INT_MAX and not visited[next_v] :
                visited[next_v] = True 
                q.append(next_v)
                dist[next_v] = dist[curr_v] + 1 
                move[next_v] = curr_v

visited[n] = True 
q.append(n)

final_pos = bfs() 

# minimum cnt
print(dist[final_pos])

# path of v 
path(final_pos) 