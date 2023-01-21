# 한쌍의 괄호 기호로 된 문자열을 VPS(Valid Parenthesis String)
# VPS를 판단하여 "YES", "NO"로 표현

import sys 
t = int(sys.stdin.readline())

for _ in range(t) :
    parenthesis = sys.stdin.readline().rstrip()
    # 2 <= p <= 50
    #  
    stack = []

    checking = True 

    for elem in parenthesis :
        if elem == '(' :
            stack.append('(')

        else :
            if len(stack) == 0 :
                checking = False
                break 

            else :
                stack.pop()
    
    if len(stack) != 0 :
        checking = False 


    if checking :
        print("YES")
    else :
        print("NO")