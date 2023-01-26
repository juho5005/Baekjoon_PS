# 최대 힙 (-를 붙여줘야 한다.)
import heapq 
import sys 

n = int(sys.stdin.readline()) # 1 <= N <= 100,000 
# O(1), O(logN), O(N), O(NlogN)
nums = [
    int(sys.stdin.readline())
    for _ in range(n)
]

# 주어진 수가 자연수이면 배열에 x라는 값을 추가
# 주어진 수가 0이면 배열에서 가장 큰 값을 출력 후 그 값을 배열에서 제거

max_heap = []

for num in nums :
    if num == 0 :
        if not max_heap : 
            print(0)
        else :
            print(-heapq.heappop(max_heap))

    else :
        heapq.heappush(max_heap, -num)
    