# 골드바흐의 추측
# 2보다 큰 모든 짝수는 두 소수의 합으로 표현 가능
# 짝수를 두 소수의 합으로 나타내는 표현을 골드바흐 파티션
# 출력하는 소수는 작은 것부터 출력하며 공백으로 구분
# 골드바흐 파티션이 여러 가지인 경우 두 소수의 차이가 가장 작은 것을 출력


import sys 
t = int(sys.stdin.readline()) # The number of test case

# 주어지는 n의 범위 : 4 <= N <= 10,000
max_n = 10000
eratos = [
    True
    for _ in range(max_n+1)
]
eratos[0], eratos[1] = False, False 

for i in range(2, int((max_n)) + 1) :
    if eratos[i] : 
        j = 2 
        while i * j <= max_n :
            eratos[i*j] = False 
            j += 1

for _ in range(t) :
    n = int(sys.stdin.readline()) # even number n is given
    
    standard = n//2 # n은 짝수이므로 반드시 정 가운데 점이 나온다.
    diff = 0
    
    while 1 :
        if eratos[standard-diff] and eratos[standard+diff] :
            print(standard-diff, standard+diff)
            break
        diff += 1
    