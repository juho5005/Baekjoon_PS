# N명 -> 반드시 짝수

# N/2명으로 이루어진
# 스타트 팀과 링크 팀으로 나눔

# s(ij) = i번 사람 + j번 사람
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 S(ij)의 합

# S(ij)와 S(ji)는 다를 수 있음

# 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 함
# 최솟값을 출력하시오

from itertools import combinations
import sys 
n = int(sys.stdin.readline()) # n is odd 

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

team_num = [
    i
    for i in range(1, n+1)
]

visited = [
    False
    for i in range(n+1)
]

ans = []

# 두 팀의 차이의 최솟값
min_diff = float('inf')

# 팀을 이루는 경우의 집합
cases = []

def ans_print() :
    case = []
    for elem in ans :
        case.append(elem)
    cases.append(case)

def choose(curr_num) :
    if curr_num == (n//2)+1 :
        ans_print()
        return 
    
    for num in team_num :
        if not visited[num] :
            if curr_num != 1 and num < ans[-1] :
                continue 
            visited[num] = True 
            ans.append(num)
            choose(curr_num+1)
            ans.pop()
            visited[num] = False
        

# implementation of func 
choose(1)

# all possible cases
l = len(cases)//2

for idx in range(l) :
    start_team = 0
    link_team = 0

    for s_elem in combinations(cases[idx], 2) :
        start_team += board[s_elem[0]-1][s_elem[1]-1]
        start_team += board[s_elem[1]-1][s_elem[0]-1]
    
    for l_elem in combinations(cases[-1-idx], 2) :
        link_team += board[l_elem[0]-1][l_elem[1]-1]
        link_team += board[l_elem[1]-1][l_elem[0]-1]

    diff = abs(start_team - link_team)

    min_diff = min(min_diff, diff)

print(min_diff)