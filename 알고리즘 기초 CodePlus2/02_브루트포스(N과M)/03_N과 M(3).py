# 1~N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

# 중복순열

ans = []

def ans_print() :
    for elem in ans :
        print(elem, end = ' ')
    print()

# curr_num번째 자리수에 들어갈 수를 고르는 함수이다.
def choose(curr_num) :
    if curr_num == m+1 :
        ans_print()
        return 
    
    for i in range(1, n+1) :
        ans.append(i)
        choose(curr_num+1)
        ans.pop()

choose(1)