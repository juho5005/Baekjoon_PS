import sys 
n = int(sys.stdin.readline())  

orders = [
    sys.stdin.readline().rstrip().split()
    for _ in range(n)
]

stack = []

for order in orders : 
    if order[0] == 'push' :
        stack.append(int(order[1]))
    
    elif order[0] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    
    elif order[0] == 'size' :
        print(len(stack))

    elif order[0] == 'empty' :
        if stack :
            print(0)
        else :
            print(1)
        
    elif order[0] == 'top' :
        if not stack :
            print(-1)
        else :
            print(stack[-1])
