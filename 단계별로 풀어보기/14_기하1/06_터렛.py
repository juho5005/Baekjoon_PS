# 조규현와 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리 계산
# 조규현 : (x1, y1) -> r1
# 백승환 : (x2, y2) -> r2

# 적이 있을 수 있는 좌표의 수 출력

import sys 
import math 
t = int(sys.stdin.readline())

for _ in range(t) :
    x1, y1, r1, x2, y2, r2 = tuple(map(int, sys.stdin.readline().split()))
    # -10,000 <= x1,y1,x2,y2 <= 10,000
    # 1 <= r1, r2 <=10,000

    # dist of two points 
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    # big r
    big_r = max(r1, r2)
    
    # small r 
    small_r = min(r1,r2)

    if d==0 and big_r==small_r :
        print(-1) # infite of possibility
    elif big_r > small_r + d :
        print(0) # none possibiltiy
    elif big_r + small_r < d :
        print(0) # none possibility
    elif big_r == small_r + d :
        print(1) 
    elif big_r + small_r == d :
        print(1)
    else :
        print(2)