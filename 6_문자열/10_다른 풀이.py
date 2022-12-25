import sys 
n = int(sys.stdin.readline()) # N <= 100

cnt = 0
for _ in range(n) : 
    s = sys.stdin.readline().rstrip()
    l = len(s) # length

    checking = True 
    
    for i in range(1, l) :
        if s[i-1] != s[i] : # 앞뒤 문자가 다르다면
            if s[i-1] in s[i+1:] : # 뒤에 s[i-1]의 문자가 존재하는 지 확인하는 것
                checking = False 
                break 
    
    if checking : 
        cnt += 1

print(cnt)
