# 쇠 막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 '( )'으로 표현
# '( )'는 레이저를 표현
# 쇠 막대기의 왼쪽 끝은 여는 괄호 '(', 오른쪽 끝은 닫힌 괄호 ')'로 표현

# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때
# 잘려진 쇠막대기 조각의 총 개수는 ?

from collections import deque 
import sys 
brackets = sys.stdin.readline().rstrip() # len(stick) <= 100,000
# O(1), O(logn), O(n), O(nlong)

dq = deque()
dq_cnt = 0 # '('를 세어줌

fragment_cnt = 0

for i in range(len(brackets)) :
    if brackets[i] == '(' :
        dq.append('(')
        dq_cnt += 1
    
    else : 
        dq.append(')')

        if brackets[i-1] == '(' :
            dq_cnt -= 1

            if dq_cnt == 0 :
                continue  
            else :
                fragment_cnt += dq_cnt 

        else :
            dq_cnt -= 1
            fragment_cnt += 1

print(fragment_cnt)    
