# 중요도를 추가한 Queue

# 1) 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인
# 2) 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치
# 그렇지 않다면, 바로 인쇄

import sys 
from collections import deque 

t = int(sys.stdin.readline())

# 중요도가 같은 문서들이 존재할 수 있음

for _ in range(t) :
    n, m = tuple(map(int, sys.stdin.readline().split()))
    # n : 문서의 개수 , m : 구하려는 문서가 몇 번째에 놓여있는지 
    importances = list(map(int, sys.stdin.readline().split()))

    dq = deque() # declaration deque

    for idx, elem in enumerate(importances) :
        dq.append((elem, idx)) # 각 카드마다 번호를 매겨둔 것
    
    cnt = 1 # count

    while 1 : 
        finish = True 

        for i in range(1, len(dq)) :
            if dq[0][0] < dq[i][0] :
                finish = False 
                break
            

        if finish :
            if dq[0][1] == m :
                print(cnt)
                break 
            else :
                cnt += 1
                dq.popleft()
        else :
            dq.append(dq[0])
            dq.popleft()