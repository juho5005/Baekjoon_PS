# 1m^2의 넓이에 자라는 참외 개수를 헤아린 후
# 참외밭의 넓이를 구하면 비레식을 이용해 참외의 총 개수를 구할 수 있다.

# 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여
# 반시계방향으로 둘레를 둘면서 지나는 변의 방향과 길이가 순서대로 주어질 때
# 참외밭에서 자라는 참외의 수를 구하라

import sys 
k = int(sys.stdin.readline()) # 1<=k<=20, 참외의 수

# 변의 방향에서
# 동쪽 : 1, 서쪽 : 2, 남쪽 : 3, 북쪽 : 4
# 변이 주어질 때 "반드시" 반시계 방향으로 주어짐

dir_side = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(6)
]

# 결국 참외밭의 넓이는 큰 직사각형에서 작은 직사각형을 뺀 넓이
# 참외밭의 모양은 ㄱ자의 방향은 다를지언정 ㄱ자의 모양은 변하지 않는다
# 결국 참외밭의 큰 직사각형의 넓이를 구하는 방법은 
# 주어진 6가지 인접한 변을 2개씩 모두 곱했을 때 곱한 값이 가장 큰 값이
# 큰 직사각형을 이루는 두 변이다.

max_area = float('-inf')
start_idx = 0

for i in range(len(dir_side)) :
    compare = dir_side[i][1] * dir_side[(i+1)%6][1]

    if compare > max_area :
        start_idx = i 
        max_area = compare 

# 큰 직사각형
big_rect = max_area 

# 작은 직사각형
# 작은 직사각형은 큰 직사각형을 셀 때의 시작 변에서 각각 3번째, 4번째 변의 길이의 곱이다
small_rect = dir_side[(start_idx+3)%6][1] * dir_side[(start_idx+4)%6][1]

# 참외밭의 넓이
melon_area = big_rect - small_rect 

# 참외밭에서 자라는 참외의 개수
print(melon_area * k)

