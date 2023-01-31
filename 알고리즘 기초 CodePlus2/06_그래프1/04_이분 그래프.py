# 그래프의 정점의 집합을 둘로 분할하여
# 각 집합에 속한 정점끼리는 서로 인접하지 않게 분할
# 이러한 그래프를 이분 그래프 (Bipartite Graph)

from collections import deque 
import sys 
k = int(sys.stdin.readline()) # test case 

for _ in range(k) :
    # vertex, line
    v, e = tuple(map(int, sys.stdin.readline().split()))

    # Declaration of queue
    q = deque()

    # 1~V : vertex
    graph = [
        []
        for _ in range(v+1)
    ] 

    visited = [
        0 
        for _ in range(v+1)
    ]

    linked_vertex = [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(e)
    ]

    def initial() :
        for s, e in linked_vertex :
            graph[s].append(e)
            graph[e].append(s)
        
        # graph sort
        for g in graph :
            g.sort()

    def bfs() :
        while q :
            curr_v = q.popleft()

            for next_v in graph[curr_v] :
                if not visited[next_v] :
                    q.append(next_v)
                    visited[next_v] = visited[curr_v] * - 1
                else :
                    if visited[next_v] == visited[curr_v] :
                        return False 
        return True 
    
    # initialize 
    initial()
    
    checking = True
    for i in range(1, v+1) :
        if not visited[i] :
            q.append(i)
            visited[i] = 1 
            
            if not bfs() :
                print("NO")
                checking = False 
                break 
    
    if checking :
        print("YES")