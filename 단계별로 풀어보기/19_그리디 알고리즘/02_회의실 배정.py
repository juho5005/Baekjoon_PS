# 한 개의 회의실을 사용하려 함
# N개의 회의에 대하여 회의실 사용표 만드려고 함.

# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어짐
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자

# 단, 회의는 한 번 시작하면 중간에 중단 x
# 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. (시작하자마자 끝나는것으로 생각)

import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 100,000 
# O(1), O(N), O(NlogN), O(logN)

conferences = []
for _ in range(n) :
    conferences.append(list(map(int, sys.stdin.readline().split())))

conferences.sort(key=lambda data:(data[1], data[0])) # 회의가 끝나는시간이 작은 순대로 오름차순

l = len(conferences)
finish_time = conferences[0][1]

# 회의의 횟수
cnt = 1

for i in range(1, l) : 
    if conferences[i][0] >= finish_time :
        finish_time = conferences[i][1]
        cnt += 1

print(cnt)