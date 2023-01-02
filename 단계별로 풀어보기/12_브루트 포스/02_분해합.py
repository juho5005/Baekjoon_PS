# 어떤 자연수 N
# 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미
# N의 분해합 = N + (N의 각 자릿수)

# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자
# N + (N의 각 자릿수)를 M이라 하고, N의 생성자라 한다.

# 어떤 자연수의 경우에는
# 생성자가 없을 수도 있고, 생성자가 여러 개인 자연수도 있다.

import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 1,000,000

checking = True

for num in range(1, n-1) :
    elem_sum = 0
    
    for elem in str(num) :
        elem_sum += int(elem)
    
    if n == (num + elem_sum) : 
        print(num)
        checking = False  
        break 

if checking : 
    print(0)