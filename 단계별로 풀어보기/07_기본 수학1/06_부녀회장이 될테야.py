# 아파트의 거주 조건
# a층의 b호에 살려면 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 데려와야 함

import sys 
t = int(sys.stdin.readline())

for _ in range(t) :
    k = int(sys.stdin.readline()) # story
    n = int(sys.stdin.readline()) # room
    
    # 0층 생성
    story_0 = [
        i
        for i in range(1, n+1)
    ]

    for i in range(k-1) :
        for j in range(1, n) :
            story_0[j] = story_0[j-1] + story_0[j]

    print(sum(story_0))    