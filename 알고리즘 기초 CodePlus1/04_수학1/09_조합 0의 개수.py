# nCm의 끝자리 0의 개수를 출력하는 프로그램 
# nCm = n! // {m! * (n-m)!}
# 0 <= m <= n <= 2,000,000,000 
# 시간복잡도 매우 큼 -> 고려대상

import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

# 끝자리에 0이 생긴다는 것은 
# 10이 곱해진다는 것이라고 볼 수 있음
# 10은 2와 5의 조합으로 생기는 것을 추론

# 즉, 2와 5의 개수의 최솟값이 끝자리 0의 개수라는 것을 알 수 있다.
# n! 의 0의 개수 에서 
# m!, (n-m)!의 0의 개수의 합을 빼주면 된다

# n! 에서 2나 5의 개수는 n을 나눠서 몫이 0이 나올 때 까지 몫의 개수를 계속 세주면 된다.

def two_count(a) :
    cnt = 0
    while a != 0 :
        cnt += (a//2)
        a //= 2
    return cnt 

def five_count(b) :
    cnt = 0
    while b != 0 :
        cnt += (b//5) 
        b //= 5
    return cnt 

print(min((two_count(n)-two_count(m)-two_count(n-m)), (five_count(n)-five_count(m)-five_count(n-m))))