# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순

import sys 
n, m  = tuple(map(int, sys.stdin.readline().split()))

# 주어지는 수는 10,000보다 작거나 같은 자연수
MAX_INT = 10000

# 주어지는 수
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

# 중복 x
# 증가하는 순서
# 앞에 나온 수보다 뒤에나오는 수가 커야한다.

ans = []
visited = [
    False 
    for _ in range(MAX_INT+1)
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
            if curr_num != 1 and ans[-1] > num :
                continue 
            visited[num] = True
            ans.append(num)
            choose(curr_num+1)
            ans.pop()
            visited[num] = False

choose(1)