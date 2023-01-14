# 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램 작성
import sys 
n = int(sys.stdin.readline()) # 3 <= N <= 100 
# O(N^4)

# 링의 반지름이 바닥에 놓은 순서대로 주어진다.
radius = list(map(int, sys.stdin.readline().split()))

compare = radius[0]

def reduction(a, b) :
    min_val = min(a, b)

    start =  2

    while 1 : 
        if start > min_val  : 
            break 
        
        if a % start == 0 and b % start == 0 : 
            a //= start 
            b //= start 
            continue 
        start += 1
    return a, b 
    
l = len(radius)
for i in range(1, l) :
    val = reduction(compare, radius[i])
    print(f'{val[0]}/{val[1]}')