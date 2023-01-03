# 7명이여야 할 난쟁이가 9명
# 일곱 난쟁이의 키의 합이 100

# 9명의 난쟁이의 키가 주어질 때 7명의 난쟁이를 찾는 프로그램 
# 7명의 난쟁이를 찾을 수 없는 경우는 존재 x
# 가능한 정답이 여러 가지일 경우, 아무거나 출력
# 난쟁이의 키를 오름차순으로 출력

import sys 
from itertools import combinations

heights = []
for _ in range(9) :
    heights.append(int(sys.stdin.readline()))


# 7가지의 모든 경우를 구하려면 combination 사용이 불가피
# 9개의 수 중 2가지 경우를 만드는 것은 2중 for문으로 가능하므로 이것을 이용
# 9개의 수의 합에서 2가지 경우의 수를 뺐을 때 값이 100이 나온다면 7난쟁이를 올바르게 찾은 것

terminater = False 

for i in range(9) :
    for j in range(i+1, 9) :
        first = heights[i]
        second = heights[j]
        if 100 == (sum(heights) - (first+second)) :
            heights.remove(first)
            heights.remove(second)
            terminater = True 
            break
    if terminater : 
        break 

heights.sort()

for elem in heights :
    print(elem)