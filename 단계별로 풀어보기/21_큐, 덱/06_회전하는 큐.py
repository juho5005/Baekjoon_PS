from collections import deque 
import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))
# N : 큐의 크기, M : 뽑아내려 하는 수

# 뽑아내려 하는 수의 위치
positions = list(map(int, sys.stdin.readline().split()))

# 1 ~ N의 리스트 생성
lst = [
    i
    for i in range(1, n+1)
]

dq = deque() # 덱 선언

# 1 ~ N의 리스트에 번호를 매긴다.
for idx, elem in enumerate(lst, start=1) :
    dq.append((elem, idx))

cnt = 0 # 뽑으려는 위치  

def left_move(point) :
    left_cnt = 0

    while 1 :
        if dq[0][1] == point : 

            for _ in range(left_cnt) :
                dq.appendleft(dq.pop())

            return left_cnt 
        else :
            left_cnt += 1
            dq.append(dq.popleft())

def right_move(point) :
    right_cnt = 0

    while 1 :
        if dq[0][1] == point : 

            for _ in range(right_cnt) :
                dq.append(dq.popleft())
            
            return right_cnt 
        else :
            right_cnt += 1
            dq.appendleft(dq.pop())


for posi in positions : 
    if dq[0][1] == posi : 
        dq.popleft()
    
    else :
        if left_move(posi) < right_move(posi) :
            cnt += left_move(posi)

            for _ in range(left_move(posi)) :
                dq.append(dq.popleft())
            dq.popleft()
        
        else :
            cnt += right_move(posi)

            for _ in range(right_move(posi)) :
                dq.appendleft(dq.pop())
            dq.popleft()
        
print(cnt)