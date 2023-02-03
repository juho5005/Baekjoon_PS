# N+1일 째 되는 날 퇴사 하기 위해 남은 N일 동안 최대한 많은 상담을 하려고 한다.
# 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아둠

# T : 상담을 완료하는데 걸리는 기간
# P : 상담을 했을 때 받을 수 있는 금액

# 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램

from collections import deque 
import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 15

consultations = deque(
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
)

# 시작 인덱스를 1로 하기 위함
consultations.appendleft([0, 0])

# 최대 이익
max_profit = float('-inf')

# 재귀 함수 earn 생성
def earn(day, money) :
    global max_profit
    max_profit = max(max_profit, money)

    if day > n :
        return 
    
    if day+consultations[day][0] <= n+1 : 
        earn(day+consultations[day][0], money + consultations[day][1])
        earn(day+1, money)
    else :
        earn(day+1, money)
    return


earn(1, 0)
print(max_profit)


