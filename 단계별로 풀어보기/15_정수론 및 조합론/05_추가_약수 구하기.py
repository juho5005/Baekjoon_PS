# 두 개의 자연수 N과 K가 주어졌을 때
# N의 약수 중 K번째로 작은 수를 출력하시오 

import math 
import sys 
n, k = tuple(map(int, sys.stdin.readline().split())) 

ans = []
# 약수를 효율적으로 구하는 방식 이용 
for i in range(1, int(math.sqrt(n)) + 1) :
    if n%i == 0 :
        ans.append(i)
        if i != (n//i) :
            ans.append(n//i)

# 약수들을 오름차순 정렬 
ans.sort() 

checking = True 
res = 0

for (idx, elem) in enumerate(ans, start=1) :
    if idx == k :
        checking = False 
        print(elem)     
        break 

if checking : 
    print(0)