# 1부터 시작해서 육각형의 모양의 인접한 방으로 이동
# 숫자 N이 주어질 때 벌집의 중앙 1에서 N번 방까지 최소 몇개의 방을 지나는가
# 시작과 끝을 포함

import sys 
n = int(sys.stdin.readline())

if n == 1 :
    print(1)
    sys.exit()

full = 6
room = 2

while 1 :
    n -= full

    if n <= 1 : 
        print(room)
        sys.exit()
    
    room += 1
    
    full += 6