# N개의 자연수 중에서 M개를 고른 수열

import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

# 수열은 사전 순(오름차순)
# 중복 허용 x

nums = list(map(int, sys.stdin.readline().split()))
# order by asc 
nums.sort()

ans = []

visited = [
    False 
    for i in range(1, 10001)
]

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

def choose(curr_num) :
    if curr_num == m+1 :
        ans_print()
        return 
    
    for num in nums :
        if not visited[num] :
            visited[num] = True 
            ans.append(num)
            choose(curr_num+1)
            ans.pop()
            visited[num] = False


choose(1)