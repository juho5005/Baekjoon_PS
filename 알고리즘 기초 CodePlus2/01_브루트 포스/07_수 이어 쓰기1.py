# 1 ~ N까지의 수를 이어서 쓰면 새로운 수를 얻을 수 있다.
# 이렇게 만들어진 새로운 수는 몇 자리 수인가 ?
# 이 수의 자릿수를 구하는 프로그램을 작성하시오.

import sys 
n = int(sys.stdin.readline()) 
# 1 <= N <= 100,000,000 
# 시간복잡도 매우 큼 
# 웬만하면 시간복잡도를 줄여야

# 1~9 -> 1 (9개)
# 10~99 -> 2 (90개)
# 100~999 -> 3 (900개)
# 1,000~9999 -> 4 (9000개)
# 10,000~99999 -> 5 (90000개)
# 100,000~999,999 -> 6 (900000개)
# ...
# 100,000,000 -> 9 (1개)

interval_edge = 10
interval = 9 

jarisu = 0

add_interval = 1 

while 1 :
    jarisu += (add_interval * interval)

    if n <= interval_edge - 1 :    
        # 뺴줘야함
        jarisu -= ((interval_edge-1 - n) * (add_interval))
        break 

    interval_edge *= 10
    interval *= 10
    add_interval += 1


print(jarisu)