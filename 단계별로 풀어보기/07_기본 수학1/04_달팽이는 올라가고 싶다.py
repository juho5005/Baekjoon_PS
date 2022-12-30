# 높이 : V
# 낮에 +A, 밤에 -B
# 정상에 도달하면 미끄러지지 않음
# 정상에 도달하기에 며칠이 걸리는가 ?

import sys 
import math
a, b, v = tuple(map(int, sys.stdin.readline().split()))
# 1 <= B < A <= V <= 1,000,000,000
# O(N)으로 해결해야함

# 식세워보기
# 구하려는 날짜 : day 
# (a * day) - (b * (day-1)) >= V 
# (a-b)*day >= V + b 
# day >= (V-b) / (a-b)

day = (v-b) / (a-b)

if day > int(day) : 
    print(int(day)+1)
else :
    print(int(day))

# 추가로 나누었을 때 정수인지 실수인지 판단할 때
# % 한 결과가 0이면 정수이고, % 한 결과가 0이 아니면 실수이다. 