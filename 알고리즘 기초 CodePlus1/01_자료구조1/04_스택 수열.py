# 1 ~ n까지의 수를 스택에 넣었다가 늘여놓음으로써,
# 하나의 수열 생성 가능
# 스택에 push 하는 순서는 오름차순을 지킨다.

import sys 
n = int(sys.stdin.readline()) # 1 <= n <= 100,000 
# O(1), O(logN), O(N), O(NlogN)

# 수열
nums = [
    int(sys.stdin.readline())
    for _ in range(n)
]

# stack 
stack = []

# means  
means = []

# num's standard
standard = 1

# positivity
checking = True 

for num in nums :

    if standard <= num :
        for i in range(standard, num + 1) :
            stack.append(i)
            means.append('+')
        
        standard = num + 1 
        stack.pop()
        means.append('-')
    
    else :
        if stack[-1] != num :
            checking = False 
        else :
            stack.pop()
            means.append('-')


if checking : 
    for elem in means :
        print(elem)

else :
    print("NO")