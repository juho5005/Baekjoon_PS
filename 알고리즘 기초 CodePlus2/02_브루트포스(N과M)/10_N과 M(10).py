# N개의 자연수 중 에서 M개를 고른 수열
# 오름차순으로 정렬

import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

nums = list(map(int, sys.stdin.readline().split()))
# 1 <= num <= 10,000
nums.sort()

INT_MAX = 10000

visited = [
    0
    for _ in range(INT_MAX+1)
]

for num in nums :
    visited[num] += 1

ans = []

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

def choose(curr_num) :
    if curr_num == m+1 :
        ans_print()
        return 
    
    prev = -1
    for num in nums :
        if visited[num] > 0 and prev != num :
            if curr_num != 1 and ans[-1] > num :
                continue 
            visited[num] -= 1
            ans.append(num)
            prev = num
            choose(curr_num+1)
            ans.pop()
            visited[num] += 1
        
choose(1)