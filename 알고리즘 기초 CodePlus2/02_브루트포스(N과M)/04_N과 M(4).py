# 1~N까지 자연수 중에서 M개를 고른 수열
# 중복 허용
# 오름차순으로 나타내야 함

from itertools import combinations_with_replacement 
import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))

ans = []

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

def choose(curr_num) :
    if curr_num == m+1 :
        ans_print()
        return 
    
    for i in range(1, n+1) :
        if curr_num != 1 and ans[-1] > i :
            continue 
        
        ans.append(i)
        choose(curr_num+1)
        ans.pop()

choose(1)