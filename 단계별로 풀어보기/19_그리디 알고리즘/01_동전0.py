# 동전은 N개의 종류 (동전은 매우 많음)
# 동전을 적절히 사용하여 가치의 합을 K로 만드려 함

# 필요한 동전 개수의 최솟값은 ?

import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))
# 1 <= N <= 10, 1 <= k <= 100,000,000

coins = []

# 필요한 동전의 개수 
cnt = 0


# 동전의 가치가 오름차순으로 주어진다.
for _ in range(n) :
    coins.append(int(sys.stdin.readline()))

# 역순으로 정렬
coins.sort(reverse=True)

for coin in coins :
    if coin > k : # 동전이 구하고자 하는 값보다 크면 바로 continue 
        continue 

    cnt += (k//coin)
    k = k%coin 

print(cnt)