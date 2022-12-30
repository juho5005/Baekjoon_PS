# 손익분기점 구하기
# A라는 고정 비용 존재.
# B라는 가변 비용 존재.
# C라는 판매 비용 존재
# 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 구하는 것
# 손익 분기점이 존재하지 않으면 -1 출력

# a + b * year < c * year 
# a < (c-b) * year
# a / (c-b) < year

import sys 
import math
a, b, c = tuple(map(int, sys.stdin.readline().split()))
# a, b, c <= 21억 이하 자연수

# B라는 가변 비용이 C라는 판매 비용보다 크다면 평생 손익분기점에 도달 불가.
if b >= c : 
    print(-1)

else :
    print((a // (c-b)) + 1)