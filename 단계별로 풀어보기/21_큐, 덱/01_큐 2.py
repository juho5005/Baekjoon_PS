from collections import deque 
import sys 

class Queue :
    def __init__(self) :
        self.dq = deque()
    
    def push(self, item) :
        self.dq.append(item)
    
    def size(self) :
        return len(self.dq)
    
    def empty(self) :
        if not self.dq : 
            return 1
        else :
            return 0 
    
    def pop(self) :
        if not self.dq :
            return -1
        else :
            return self.dq.popleft()
            
    
    def front(self) :
        if not self.dq :
            return -1
        else :
            return self.dq[0]

    def back(self) :
        if not self.dq :
            return -1
        else :
            return self.dq[-1]
    
# 큐 선언
q = Queue() 

n = int(sys.stdin.readline()) # 1 <= n <= 2,000,000 (명령의 수)

for _ in range(n) :
    order = sys.stdin.readline().rstrip().split()

    if len(order) == 2 : 
        num = int(order[1])
        order = order[0]
    else :
        order = order[0]
    
    if order == 'push' :
        q.push(num)
    
    elif order == 'pop' :
        print(q.pop())
    
    elif order == 'size' :
        print(q.size())
    
    elif order == 'empty' :
        print(q.empty())
    
    elif order == 'front' :
        print(q.front())
    
    else :
        print(q.back())
    