import heapq 
import sys 

n = int(sys.stdin.readline()) # 1 <= N <= 100,000
# O(1), O(logN), O(N), O(NlogN)

nums = [
    int(sys.stdin.readline())
    for _ in range(n)
]

# x가 자연수이면 배열에 x를 추가
# x가 0이면 배열에서 가장 작은 값을 출력 후 그 값을 배열에서 제거 

min_heap = []

for num in nums : 
    if num == 0 :
        if not min_heap :
            print(0)
        else :
            print(heapq.heappop(min_heap))
    elif num > 0 :
        heapq.heappush(min_heap, num)