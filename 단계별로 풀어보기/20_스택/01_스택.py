# 정수를 저장하는 스택을 구현 후, 명령을 처리하는 프로그램 작성

import sys 
n = int(sys.stdin.readline()) 

class Stack : 
    def __init__(self) :
        self.items = []
    
    def push(self, item) :
        self.items.append(item)
    
    def size(self) :
        return len(self.items)

    def empty(self) :
        if self.items : 
            return 0 
        else :
            return 1

    def pop(self) :
        if not self.items :
            return -1 
        else :
            return self.items.pop()
    
    def top(self) :
        if not self.items :
            return -1 
        else :
            return self.items[-1]

# 스택 선언
s = Stack()

for _ in range(n) :
    order = sys.stdin.readline().rstrip().split()

    if len(order) == 2 :
        num = int(order[1])
    
    order = order[0]

    if order == 'push' :
        s.push(num)

    elif order == 'size' :
        print(s.size())
    
    elif order == 'empty' :
        print(s.empty())
    
    elif order == 'pop' :
        print(s.pop())
    
    else :
        print(s.top())