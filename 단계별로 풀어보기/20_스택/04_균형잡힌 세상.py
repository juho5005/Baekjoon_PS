# 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램 
# 괄호의 종류로는 '소괄호', '대괄호' => 2가지

# 소괄호는 소괄호끼리, 대괄호는 대괄호끼리
# 모든 오른쪽 괄호들은 짝을 이루는 왼쪽 괄호가 존재함 
# 괄호들은 1:1 matching만 가능
# 짝을 이루는 두 괄호가 있을 때 그 사이에 있는 문자열도 균형이 잡혀야 함

# 균형잡힌 문자열인지 아닌지 판별 

import sys 

while True :
    balanced_string = sys.stdin.readline().rstrip() # 100글자 이하 : 시간복잡도 고려 x
    
    if balanced_string == '.' :
        break 
    
    stack = [] # 괄호 관리

    decision = True # 결정 

    for elem in balanced_string :
        # 소괄호일 경우
        if elem == '(' :
            stack.append(elem)
        elif elem ==')' : 
            if len(stack) == 0 :
                decision = False 
                break 
            else :
                if stack[-1] != '(' :
                    decision = False 
                    break 
                stack.pop()

        # 대괄호일 경우
        if elem == '[' :
            stack.append(elem)
        elif elem ==']' :
            if len(stack) == 0 :
                decision = False 
                break 
            else :
                if stack[-1] != '[' :
                    decision = False 
                    break 
                stack.pop()
    
    # 반복문이 끝난 후 각 스택들이 비어있는지 확인
    if len(stack) != 0 :
        decision = False 
    
    if decision :
        print("yes")
    else :
        print("no")

