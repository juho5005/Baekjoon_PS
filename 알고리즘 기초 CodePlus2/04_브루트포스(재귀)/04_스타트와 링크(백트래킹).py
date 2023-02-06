import sys 
n = int(sys.stdin.readline()) # n is odd 

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

visited = [
    False
    for i in range(n+1)
]

min_diff = float('inf')

def dfs(depth, idx) :
    global min_diff 

    if depth == n//2 :
        st, lt = 0, 0

        for i in range(1, n+1) :
            for j in range(1, n+1) :
                if visited[i] and visited[j] :
                    st += board[i-1][j-1]
                
                elif not visited[i] and not visited[j] :
                    lt += board[i-1][j-1]

        min_diff = min(min_diff, abs(st-lt))
        return 

    for i in range(idx, n+1) :
        if not visited[i] :
            visited[i] = True 
            dfs(depth+1, i+1)
            visited[i] = False 

dfs(0, 1)
print(min_diff)