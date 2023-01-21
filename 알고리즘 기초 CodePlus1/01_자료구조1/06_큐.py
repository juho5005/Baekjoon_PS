from collections import deque 
import sys 
n = int(sys.stdin.readline())

orders = [
    sys.stdin.readline().rstrip().split()
    for _ in range(n)
]

dq = deque()

for order in orders :
    if order[0] == 'push' :
        dq.append(int(order[1]))
    
    elif order[0] == 'pop' :
        if not dq :
            print(-1)
        else :
            print(dq.popleft())
    
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