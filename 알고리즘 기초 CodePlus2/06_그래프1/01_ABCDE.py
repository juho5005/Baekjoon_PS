# 0번 ~ N-1번 
# 친구관게를 가진 ABCDE가 존재하는지 구하려고 한다.
# dfs를 했을 때 깊이가 4이상일 시 친구관계가 존재한다고 할 수 있다.

# dfs

import sys
sys.setrecursionlimit(10**6)
n, m = tuple(map(int, sys.stdin.readline().split()))

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

graph = [
    []
    for _ in range(n)
]

visited = [
    False 
    for _ in range(n)
]

# 정답의 존재 유무
ans = False 

def initial() :
    for s, e in linked_vertex :
        graph[s].append(e)
        graph[e].append(s)
    
    # sort by asc 
    for g in graph :
        g.sort()

def dfs(curr_v, cnt) :
    global ans 

    if cnt == 4 :
        ans = True 
        return 
    
    for next_v in graph[curr_v] :
        if not visited[next_v] :
            visited[next_v] = True 
            dfs(next_v, cnt+1)
            visited[next_v] = False 

# initialize 
initial()

for root_vertex in range(n) :
    visited[root_vertex] = True 
    dfs(root_vertex, 0)
    visited[root_vertex] = False 

    if ans :
        break 

# finial judge 
if ans :
    print(1)
else :
    print(0)