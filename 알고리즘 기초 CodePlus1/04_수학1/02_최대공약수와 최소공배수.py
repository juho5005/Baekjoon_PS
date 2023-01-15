import sys 
a, b = tuple(map(int, sys.stdin.readline().split())) 

# 최대공약수 (the greatest common divisor)
def gcd(a, b) :
    while b > 0 : 
        a, b = b, a % b 
    return a 

# 최소공배수 (the least common multiple)
def lcm(a, b) :
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))