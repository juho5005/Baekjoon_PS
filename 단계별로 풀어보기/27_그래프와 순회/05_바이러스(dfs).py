# 1번 컴퓨터가 바이러스에 걸렸을 때
# 네트워크 상에서 연결되어 있는 정보가 주어질 때 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력

# dfs (인접 리스트)

import sys 
sys.setrecursionlimit(10**6)

# 컴퓨터의 수 (1~n번까지)
n = int(sys.stdin.readline()) 

# 연결된 컴퓨터 쌍의 수 
m = int(sys.stdin.readline())

linked_vertex = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

# 인접 리스트 이용 
graph = [
    []
    for _ in range(n+1)
]

visited = [
    False 
    for _ in range(n+1)
]

computers_num = 0

def initial() :
    for s,e in linked_vertex :
        graph[s].append(e)
        graph[e].append(s)
    
    # dfs is proceeded by asc 
    for g in graph :
        g.sort()
    

def dfs(vertex) :
    global computers_num 

    for curr_v in graph[vertex] :
        if not visited[curr_v] :
            computers_num += 1
            visited[curr_v] = True 
            dfs(curr_v)

root_vertex = 1 
visited[root_vertex] = True 

# functions
initial()
dfs(root_vertex) 

print(computers_num)