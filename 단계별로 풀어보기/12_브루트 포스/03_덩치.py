# 사람의 덩치 = (키, 몸무게)
# A : (x, y) / B : (p, q) 중 x > p, y > q이면 A가 B보다 덩치가 크다고 말할 수 있다.

# N명의 집단에서 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다.
# 자신보다 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.

import sys 
n = int(sys.stdin.readline())  # 2 <= N <= 50

bodies = []
for _ in range(n) :
    bodies.append(list(map(int, sys.stdin.readline().split())))

# length
l = len(bodies)

for i in range(l) :
    rank = 1
    for j in range(l) :
        if i == j :
            continue 
        if (bodies[j][0] > bodies[i][0]) and (bodies[j][1] > bodies[i][1]) :
            rank += 1
    
    print(rank, end = ' ')