import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

ans = []

visited = [
    False 
    for i in range(n+1)
]

def print_ans() :
    for elem in ans :
        print(elem, end = ' ')
    print()


# def choose()
# curr_num 번째 위치에 1~N의 숫자를 고르는 함수
def choose(curr_num) :
    if curr_num == m+1 : 
        print_ans()
        return 
    
    for i in range(1, n+1) :
        if not visited[i] :
            visited[i] = True
            ans.append(i)
            choose(curr_num+1)
            ans.pop()
            visited[i] = False 
            
# Implement the function
choose(1)


