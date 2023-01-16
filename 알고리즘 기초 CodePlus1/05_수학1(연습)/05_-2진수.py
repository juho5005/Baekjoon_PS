# -2진수
# -2진수의 규칙을 찾아보니 -2로 나누는 수가 홀수일 때 
# 몫과 -2를 곱했을 때 그 홀수보다 1 작은수가 나오도록 만들고 나머지는 1로 설정
# 몫이 0이 됐을 때를 종료시점으로 삼으면 될듯하다.

import sys 
n = int(sys.stdin.readline()) # 10진법으로 표현된 수 N 

if n==0:
    print(0)
    sys.exit()

def minus_binary(n) :
    # 결과값
    res = ''

    # 몫 초기설정
    share = n

    while share != 0 : 
        
        if share%2 == 1 : # n이 홀수라면 
            share = ((share-1)//2) * -1
            res_ = 1 # 나머지는 무조건 1 
        
        else : # n이 짝수라면 
            share = (share//2) * -1 
            res_ = 0
    
        res = str(res_) + res # 이진수 이므로 거꾸로 더해준다.
    
    return res 

print(minus_binary(n))