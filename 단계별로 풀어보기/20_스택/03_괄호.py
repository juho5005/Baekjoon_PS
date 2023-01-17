# 괄호 문자열
# Parenthesis String, (Ps)
# '('와 ')' 만으로 구성된 문자열 = Valid PS(VPS)

# 주어진 괄호 문자열이 VPS인지 아닌지 판별하여 결과를 YES, NO로 나타내야 한다.

import sys 
t = int(sys.stdin.readline())

for _ in range(t) :
    p_string = sys.stdin.readline().rstrip()
    
    stack = [] 
    decision = True

    for elem in p_string :
        if elem == '(' :
            stack.append(elem)

        else :
            if len(stack) == 0 :
                decision = False 
                break 
            else :
                stack.pop()
        
    # '('만 계속해서 나온 경우에는 판별에 걸리지 않기 때문에
    # 반복문이 종료된 후 스택이 비어있음을 확인해야 한다.
    if len(stack) != 0 :
        decision = False 
    
    if decision : 
        print("YES")
    else :
        print("NO")