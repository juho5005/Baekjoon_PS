# 빨간 실선은 
# 행성게 진입/이탈 횟수를 최소화하는 경로

# 원은 행성계의 경계를 의미함

# 은하수 지도, 출발점, 도착점이 주어질 때
# 어린왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하라
# 행성계의 경계가 맞닿거나 서로 교차하는 경우는 존재 x
# 출발점이나 도착점이 행성계에 겹친 경우도 존재 x

import math 
import sys 
t = int(sys.stdin.readline()) 

def find_r(x1,y1,x2,y2) :
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

for _ in range(t) :
    # start_point, end_point
    x1, y1, x2, y2 = tuple(map(int, sys.stdin.readline().split()))

    # the number of planet 
    n = int(sys.stdin.readline()) 
    
    planet_pos_d = [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(n)
    ]

    if x1==x2 and y1==y2 :
        print(0)
        continue 

    cnt = 0

    for x,y,r in planet_pos_d :
        if find_r(x1,y1,x,y) < r and find_r(x2,y2,x,y) < r :
            continue 
        if find_r(x1,y1,x,y) < r :
            cnt += 1
        if find_r(x2,y2,x,y) < r :
            cnt += 1
    
    print(cnt)
