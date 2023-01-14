# ATM에 N명의 사람들이 줄을 선다.
# 1번 ~ N번의 번호가 새겨짐

# i번 사람이 돈을 인출하는데 걸리는 시간 = P(i)분

# 사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라진다.

# 줄을 설 때, 돈을 뽑는 시간이 오래 걸리는 사람일 수록 후방에 배치해야
# 기다리는 총 시간이 줄어들게 될 것 같다.

# 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하시오 

import sys 
n = int(sys.stdin.readline()) # 1 <= N <=1,000 
# O(N^2), O(N^2logN)

times = list(map(int, sys.stdin.readline().split()))

# sort with ascending
times.sort()

# the time requied with min
cumulative_time = 0
min_time = 0


for time in times :
    cumulative_time += time 
    
    min_time += cumulative_time 

print(min_time)
    

