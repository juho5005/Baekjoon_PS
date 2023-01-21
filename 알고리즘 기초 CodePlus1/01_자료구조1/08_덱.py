from collections import deque 
import sys

n = int(sys.stdin.readline())

orders = [
    sys.stdin.readline().rstrip().split()
    for _ in range(n)
]

dq = deque()

for order in orders :
    if order[0] == 'push_front' :
        dq.appendleft(int(order[1]))
    
    elif order[0] == 'push_back' :
        dq.append(int(order[1]))
    
    elif order[0] == 'pop_front' :
        if not dq :
            print(-1)
        else :
            print(dq.popleft())
    
    elif order[0] == 'pop_back' :
        if not dq :
            print(-1)
        else :
            print(dq.pop())
    
    elif order[0] == 'size' :
        print(len(dq))
    
    elif order[0] == 'empty' :
        if not dq :
            print(1)
        else :
            print(0)
    
    elif order[0] == 'front' :
        if not dq :
            print(-1)
        else :
            print(dq[0])
    
    elif order[0] == 'back' :
        if not dq :
            print(-1)
        else :
            print(dq[-1])