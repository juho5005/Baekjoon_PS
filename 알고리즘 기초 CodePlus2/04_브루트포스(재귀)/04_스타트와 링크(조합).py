
from itertools import combinations 
import sys 
n = int(sys.stdin.readline()) # N : odd_num 

graph = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
] # 1 <= s(ij) <= 100

members = [
    i
    for i in range(1, n+1)
]

min_diff = float('inf')

# st : start team
# lt : link team
for st in combinations(members, n//2) :
    start_ability = 0
    link_ability = 0

    lt = list(set(members) - set(st))

    for s in combinations(st, 2) :
        start_ability += graph[s[0]-1][s[1]-1] + graph[s[1]-1][s[0]-1]

    for l in combinations(lt, 2) :
        link_ability += graph[l[0]-1][l[1]-1] + graph[l[1]-1][l[0]-1]
    
    diff = abs(start_ability - link_ability)

    min_diff = min(min_diff, diff)

print(min_diff)