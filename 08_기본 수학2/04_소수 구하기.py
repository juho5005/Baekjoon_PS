# M이상 N이하의 소수를 모두 출력하는 프로그램
# 1 <= M <= N <= 1,000,000

import sys 
m, n = tuple(map(int, sys.stdin.readline().split()))
# O(N), O(NlogN), O(logN), O(1)의 시간복잡도를 갖는다.

# 1 ~ n의 수를 True로 init 
eratos = [
    True 
    for i in range(n+1) 
] 
# 0과 1은 소수가 아니므로 처음부터 아니라고 Init
eratos[0] = False 
eratos[1] = False

# 에라토스테네스의 체 
# 자기 자신을 제외한 배수가 모두 소수가 아니고
# sqrt(n) + 1 까지만 경우를 따져보면 된다.

for i in range(2, int((n)**(1/2)) + 1) :
    if eratos[i] : # 이미 False가 있다면, 굳이 에라토네스의 채를 사용할 필요 X
        j = 2
        while i * j <= n : 
            eratos[i*j] = False 
            j += 1

for idx in range(m, n+1) :
    if eratos[idx] :
        print(idx)