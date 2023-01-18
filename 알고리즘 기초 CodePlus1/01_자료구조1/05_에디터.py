from collections import deque 
import sys 

string = sys.stdin.readline().rstrip() 

m = int(sys.stdin.readline())

orders = [
    tuple(sys.stdin.readline().rstrip().split())
    for _ in range(m)
]

# 커서를 기준으로 왼쪽이 left_dq, 커서를 기준으로 오른쪽이 right_dq 
left_dq = deque(string)
right_dq = deque()


for order in orders :
    if order[0] == 'L' :
        if not left_dq : # 왼쪽 덱이 비었을 때 = 커서가 맨 왼쪽일 때
            continue 
        right_dq.appendleft(left_dq.pop())
    
    elif order[0] == 'D' :
        if not right_dq : # 오른쪽 덱이 비었을 때 = 커서가 맨 뒤쪽일 때
            continue 
        left_dq.append(right_dq.popleft())

    elif order[0] == 'B' :
        if not left_dq : # 왼쪽 덱이 비었을 때 = 커서가 맨 왼쪽일 때
            continue 
        left_dq.pop()
    
    else :
        left_dq.append(order[1])

new_dq = left_dq + right_dq 

for elem in new_dq :
    print(elem, end = '')