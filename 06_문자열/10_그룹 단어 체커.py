# 그룹단어 
# 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우의 단어를 말함 

import sys 
n = int(sys.stdin.readline()) # N <= 100

cnt = 0
for _ in range(n) : 
    s = sys.stdin.readline().rstrip()
    l = len(s) # length

    checking = True
    for i in range(1, l) :
        if s.find(s[i-1]) > s.find(s[i]) :
            checking = False 
    
    if checking : 
        cnt += 1
    
print(cnt)