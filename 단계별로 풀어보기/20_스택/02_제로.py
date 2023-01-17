# 재현이가 잘못된 수를 부를 때마다 0을 외쳐서
# 가장 최근에 재민이가 쓴 수를 지우게 만든다.
# 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고자 함

import sys 
k = int(sys.stdin.readline())
# 1 <= k <= 100,000
# O(1), O(logN), O(NlogN), O(N)

stack = []

for _ in range(k) :
    num = int(sys.stdin.readline())

    if num != 0 :
        stack.append(num)
    else :
        stack.pop()

print(sum(stack))