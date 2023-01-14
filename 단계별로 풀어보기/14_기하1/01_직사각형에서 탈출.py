# 현재 (x, y)에 위치
# 직사각형은 각 변이 좌표축에 평행
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램 작성

import sys 
x, y, w, h = tuple(map(int, sys.stdin.readline().split()))

# 왼쪽 아래 꼭짓점 (0, 0)
# 오른쪽 위 꼭짓점 (w, h)

# 1) 오른쪽 아래 꼭짓점 (w, 0)
# 2)  왼쪽  위  꼭짓점 (0, h)

min_dist = sys.maxsize 

print(min(min_dist, w-x, h-y, x, y))