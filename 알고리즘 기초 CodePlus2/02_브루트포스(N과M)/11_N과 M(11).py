# N개의 자연수 중에서 M개를 고른 수열 
# 중복 허용

import sys
n, m = tuple(map(int, sys.stdin.readline().split()))

nums = list(map(int, sys.stdin.readline().split()))
nums.sort() # order by asc 

ans = []

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

def choose(curr_num) :
    if curr_num == m+1 :
        ans_print()
        return 
    
    prev = - 1
    for num in nums :
        if prev == num :
            continue 
        
        prev=num
        ans.append(num)
        choose(curr_num+1)
        ans.pop()

choose(1)