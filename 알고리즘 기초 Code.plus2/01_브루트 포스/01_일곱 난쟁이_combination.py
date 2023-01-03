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

seven_height = 100

# 모든 경우를 다 따져보면 간단함
# combinations 모듈 이용
possible_lst = []
for elem in combinations(heights, 7) :
    if sum(elem) == seven_height :
        
        for num in elem :
            possible_lst.append(num)
        break

possible_lst.sort() # 오름차순 정렬

# 출력
for elem in possible_lst :
    print(elem)