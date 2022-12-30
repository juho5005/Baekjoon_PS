# x좌표가 증가하는 순
# x좌표가 같으면 y좌표가 증가하는 순으로 정렬 

import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 100,000 

# 좌표
coordinates = []

for _ in range(n) :
    coordinates.append(list(map(int, sys.stdin.readline().split())))

# lambda를 이용한 정렬 
sorted_coordinates = sorted(coordinates, key=lambda data:(data[0], data[1]))

for elem in sorted_coordinates : 
    print(*elem)