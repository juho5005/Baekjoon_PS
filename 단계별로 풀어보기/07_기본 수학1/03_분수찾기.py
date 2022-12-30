# 분수를 지그재그 형태로 세어줌
# X가 주어졌을 때, X번 째 분수를 구하는 프로그램 작성 

import sys 
x = int(sys.stdin.readline()) # 1 <= x <= 10,000,000
# O(1)으로 풀어야 된다고 판단 : 시간 제한 존재

# 묶음에 따라 세어주는 방향이 다른 것을 확인할 수 있음
# 개수가 짝수개면 아래로
# 개수가 홀수개면 위로

bundle = 1 
start = 1
plus = 1

while 1 : 
    if start >= x :
        if bundle % 2 == 1 : # when bundle is odd
            print(f'{1+(start-x)}/{bundle-(start-x)}')
        else : # when bundle is even
            print(f'{bundle-(start-x)}/{1+(start-x)}')
        sys.exit()
    plus += 1
    start += plus 
    bundle += 1