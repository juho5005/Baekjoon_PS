# 각 층에 W개의 방, H층 건물 (1<=H,W<=99)
# 방 번호 : YXX, YYXX 두 가지 경우
# 엘레베이터는 고려 X, 아래 층 선호

import sys
t = int(sys.stdin.readline())

for _ in range(t) :
    h, w, n = tuple(map(int, sys.stdin.readline().split()))

    if n % h == 0 :
        room_h = h
        room_w = n//h

    else :
        room_w = n//h + 1
        room_h = n%h
    
    if room_w < 10 :
        print(f'{room_h}{0}{room_w}')
    else :
        print(f'{room_h}{room_w}')