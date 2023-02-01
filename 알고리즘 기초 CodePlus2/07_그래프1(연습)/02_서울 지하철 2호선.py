# 노선도가 주어질 때 각 역과 순환선 사이의 거리 구하기

# 역 A와 순환선 사이의 거리는 
# A와 순환선에 속하는 역 사이의 거리 중 최솟값

# BFS

# pypy 제출본

from collections import deque 
import sys 
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline()) # 3 <= N <= 3000

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# graph 
graph = [
    []
    for _ in range(n+1)
]

# whether visit
visited = [
    False
    for _ in range(n+1)
]

# cycle station
cycle_station = [
    False 
    for i in range(n+1)
]

check = [
    -1
    for _ in range(n+1)
]

# initialize
def initial() :
    for s, e in linked_vertex :
        graph[s].append(e)
        graph[e].append(s)
        
# check cycle
def dfs(curr_v, start, cnt) :
    global cycle 

    if cycle :
        return 

    # visited station >= 2 and curr_v == start 
    if curr_v == start and cnt >= 2 :
        cycle = True 
        return 
    
    for next_v in graph[curr_v] :
        if not visited[next_v] :
            visited[next_v] = True 
            dfs(next_v, start, cnt+1)
        else :
            if next_v == start and cnt >= 2 :
                dfs(next_v, start, cnt)

def distance_station() :
    global check 

    q = deque()

    # 순환역에 속하는 역은 모두 거리가 0
    for i in range(1, n+1) :
        if cycle_station[i] :
            check[i] = 0
            q.append(i)
    
    while q :
        curr_v = q.popleft()

        for next_v in graph[curr_v] :
            if check[next_v] == -1 :
                q.append(next_v)

                check[next_v] = check[curr_v] + 1
    
    for elem in check[1:] :
        print(elem, end = ' ')

# finalize
initial()

for i in range(1, n+1) :
    # whether visited 
    visited = [
        False 
        for _ in range(n+1)
    ]

    # whether cycle
    cycle = False 

    # check cycle
    visited[i] = True 
    dfs(i, i, 0)

    # check dist
    if cycle :
        cycle_station[i] = True 

distance_station()