import sys 
n = int(sys.stdin.readline())

# 1 <= N <= 10,000,000 
# N의 범위가 매우 크므로 O(1)로 해결해야 하므로 카운팅 정렬 사용
N = 10000

count_nums = [0 
    for _ in range(N+1)
    ]

# 미연에 설정한 배열에 개수만큼 더해준다.
for _ in range(n) :
    count_nums[int(sys.stdin.readline())] += 1

# 출력
for i in range(1, N+1) :
    if count_nums[i] == 0 :
        continue 
    
    for j in range(count_nums[i]) :
        print(i)