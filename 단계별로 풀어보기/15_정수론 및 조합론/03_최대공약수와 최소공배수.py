import sys 

a, b = list(map(int, sys.stdin.readline().split()))

# 최대공약수 (the greatest common divisor)
def gcd(a, b) :
    min_num = min(a, b)
    result = 0
    
    for i in range(min_num, 0, -1) : # 최대 공약수를 찾으므로 반대로 돌리면 시간단축 가능
        if a % i == 0 and b % i == 0 :
            result = i 
            break
    
    return result 

# 최소공배수 (the least common multiple)
def lcm(a, b) :
    min_num = min(a, b)
    result = 1

    start = 2 

    while 1 : 
        if start > min_num : 
            break 
        
        if a % start == 0 and b % start == 0 :
            a //= start 
            b //= start
            result *= start 
            continue 

        start += 1

    result *= (a*b)
    return result


# 최대공약수 출력
print(gcd(a, b))

# 최소공배수 출력
print(lcm(a, b))