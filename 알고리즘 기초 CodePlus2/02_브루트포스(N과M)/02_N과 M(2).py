import sys
n, m = tuple(map(int, sys.stdin.readline().split()))

ans = []

visited = [
    False
    for _ in range(n+1)
]

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

# curr_num번째 자리의 수를 구하는 함수
def choose(curr_num) :
    if curr_num == m+1 :
        ans_print()
        return 
    
    for i in range(1, n+1) :
        if not visited[i] :
            if curr_num != 1 and ans[-1] > i :
                continue
            visited[i] = True 
            ans.append(i)
            choose(curr_num+1)
            ans.pop()
            visited[i] = False
        
choose(1)