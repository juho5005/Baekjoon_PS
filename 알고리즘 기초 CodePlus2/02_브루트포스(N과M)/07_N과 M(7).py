# N개의 자연수 중 M개를 고른 수열
# 중복 허용

import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

# n개의 수
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

ans = []

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

def choose(curr_num) :
    if curr_num == m+1:
        ans_print()
        return 
    
    for num in nums :
        ans.append(num)
        choose(curr_num+1)
        ans.pop()

choose(1)