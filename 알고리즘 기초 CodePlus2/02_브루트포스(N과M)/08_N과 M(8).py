# N개의 자연수 중에서 M개를 고른 수열
# 중복 허용
# 오름차순

import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

ans = []

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

def choose(curr_num) :
    if curr_num == m+1 :
        ans_print()
        return 

    for num in nums :
        if curr_num != 1 and ans[-1] > num :
            continue 
        ans.append(num)
        choose(curr_num+1)
        ans.pop()

choose(1)