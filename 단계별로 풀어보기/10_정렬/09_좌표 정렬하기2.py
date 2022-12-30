# 2차원 평면 위에 점 N개가 주어진다.
# y좌표가 증가하는 순, y좌표가 같으면 x좌표가 증가하는 순으로 작성

import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 100,000 
# O(1), O(logN), O(N), O(NlogN)

coordinates = []
for _ in range(n) :
    coordinates.append(list(map(int, sys.stdin.readline().split())))

coordinates.sort(key=lambda data:(data[1], data[0]))

for elem in coordinates :
    print(*elem)