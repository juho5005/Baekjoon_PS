# Stack : LIFO(Last In First Out)

# 1~n 까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 하나의 수열 생성 가능
# 스택애 push하는 순서는 반드시 오름차순을 지키도록 함

# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지 알아낼 수 있다.

# 이를 계산하는 프로그램 작성 

import sys 
n = int(sys.stdin.readline()) # 1 <= n <= 100,000 

# push -> '+'
# pop -> '-'

nums = [
    int(sys.stdin.readline())
    for _ in range(n)
]

# 스택
stack = []

# 계산
calculation = []

# 포인트 지점
point = 1

# 결정
decision = True 

for num in nums : 
    if num >= point :
        for i in range(point, num+1) :
            stack.append(i)
            calculation.append('+')
        
        stack.pop()
        calculation.append('-')
        point = num+1
        
    else :
        if num != stack[-1] :
            decision = False 
            break 
        else :
            stack.pop()
            calculation.append('-')

if decision : 
    print(*calculation)
else :
    print("NO")