# 후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때 
# 그 식을 계산하는 프로그램 작성

import sys 

# 피연산자의 개수 
n = int(sys.stdin.readline())

# 후위표기식 
rear_expression = sys.stdin.readline().rstrip()

# matching 
dic = {}

standard = ord('A')
for _ in range(n) :
    dic[chr(standard)] = int(sys.stdin.readline())
    standard += 1


stack = []

idx = 0
l = len(rear_expression)

while idx < l :
    if ord(rear_expression[idx]) >= ord('A') and ord(rear_expression[idx]) <= ord('Z') :
        stack.append(dic[rear_expression[idx]])
    
    else : 
        if rear_expression[idx] == '*' :
            num1 = stack.pop()
            num2 = stack.pop()
            val = num1 * num2
            stack.append(val)
        
        elif rear_expression[idx] == '/' :
            num1 = stack.pop()
            num2 = stack.pop()
            val = num2 / num1
            stack.append(val)

        elif rear_expression[idx] == '+' :
            num1 = stack.pop()
            num2 = stack.pop()
            val = num1 + num2
            stack.append(val)

        elif rear_expression[idx] == '-' :
            num1 = stack.pop()
            num2 = stack.pop()
            val = num2 - num1
            stack.append(val)
        
        
    idx += 1

res = round(stack[0], 3)

print(f'{res:.2f}')