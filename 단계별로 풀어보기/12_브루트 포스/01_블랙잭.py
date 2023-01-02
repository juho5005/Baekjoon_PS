# 카드의 합이 21을 넘지않는 선에서, 카드의 합을 최대한 크게 만드는 게임
# N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
# 그런 후에 딜러는 숫자 M을 크게 외친다.

# 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 고른다.
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

import sys 
n, m = tuple(map(int, sys.stdin.readline().split())) 
# 3 <= N <= 100 -> O(N^4)
# 10 <= N <= 300,000 -> O(1), O(logN), O(N), O(NlogN)

cards = list(map(int, sys.stdin.readline().split()))

# 카드의 합의 최댓값
max_sum = -sys.maxsize 

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            if (cards[i] + cards[j] + cards[k]) <= m : 
                max_sum = max(max_sum, (cards[i] + cards[j] + cards[k]))

print(max_sum)