# 커트라인 = 상을 받는 사람들 중 점수가 가장 낮은 사람의 점수

import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))
scores = list(map(int, sys.stdin.readline().split()))

scores.sort()
l = len(scores) - 1

print(scores[l-k+1])