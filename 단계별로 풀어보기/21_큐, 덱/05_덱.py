from collections import deque 
import sys 

n = int(sys.stdin.readline()) 
# 1 <= 10,000 

class deq :
    def __init__(self) :
        self.dq = deque()
    def push_front(self, item) :
        self.dq.appendleft(item)
    def push_back(self, item) :
        self.dq.append(item)
    def pop_front(self) :
        if not self.dq :
            return -1 
        return self.dq.popleft()
    def pop_back(self) :
        if not self.dq :
            return -1 
        return self.dq.pop()
    def size(self) :
        return len(self.dq)
    def empty(self) :
        if self.dq :
            return 0
        else :
            return 1 
    def front(self) :
        if not self.dq :
            return -1 
        return self.dq[0]
    def back(self) :
        if not self.dq :
            return -1 
        return self.dq[-1]

dq_ = deq() 

for _ in range(n) :
    orders = sys.stdin.readline().rstrip().split()

    if len(orders) == 2 :
        order = orders[0]
        num = int(orders[1])
    else :
        order = orders[0]
    
    if order == 'push_front' :
        dq_.push_front(num)
    elif order == 'push_back' :
        dq_.push_back(num)
    elif order == 'pop_front' :
        print(dq_.pop_front())
    elif order == 'pop_back' :
        print(dq_.pop_back())
    elif order == 'size' :
        print(dq_.size())
    elif order == 'empty' :
        print(dq_.empty())
    elif order == 'front' :
        print(dq_.front())
    else :
        print(dq_.back())