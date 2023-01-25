# 문자열 S의 모든 접미사를 사전순으로 정렬 

import sys 
s = sys.stdin.readline().rstrip() # s <= 1000 
# O(N^3)

# string s' length
l = len(s)

# suffix's list 
suffixes = []

start = 0
for _ in range(l) :
    suffixes.append(s[start:])
    start += 1

suffixes.sort()

for elem in suffixes :
    print(elem)