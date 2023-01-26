# 절댓값 힙
# 배열에 정수 x를 넣음
# 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거
# 이 때, 절댓값이 가장 작은 값이 여러 개일 때는 가장 작은수를 출력 후 배열에서 제거 

import sys 
import heapq 

n = int(sys.stdin.readline()) # 1 <= N <= 100,000

nums = [
    int(sys.stdin.readline())
    for _ in range(n)
]

# 0이 주어진 횟수만큼 답을 출력
# 0이 주어졌을 때 배열이 비어있는 경우엔 0을 출력한다.

abs_heap = []

for num in nums :
    if num == 0 :
        if not abs_heap :
            print(0)
        else :
            tp = heapq.heappop(abs_heap)
            print(tp[1])

    else :
        heapq.heappush(abs_heap, (abs(num), num))