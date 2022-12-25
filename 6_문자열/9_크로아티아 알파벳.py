# c=, s=, dz=, z=
# c-, d-
# lj, nj 

import sys 
s = sys.stdin.readline().rstrip()

l = len(s)
cnt = l # 개수를 빼줄 생각

for i in range(1, l) :
    if s[i] == '=' :
        if s[i-1] == 'c' :
            cnt -= 1
        if s[i-1] == 's' :
            cnt -= 1
        if s[i-1] == 'z' :
            if s[i-2] == 'd' :
                cnt -= 2
            else :
                cnt -= 1
    
    elif s[i] == '-' :
        if s[i-1] == 'c' :
            cnt -= 1
        if s[i-1] == 'd' :
            cnt -= 1
    
    elif s[i] == 'j' :
        if s[i-1] == 'l' :
            cnt -= 1
        if s[i-1] == 'n' :
            cnt -= 1

print(cnt)