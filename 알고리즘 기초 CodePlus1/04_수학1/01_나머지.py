import sys 
a, b, c = tuple(map(int, sys.stdin.readline().split())) # 2 <= A,B,C <= 10,000

print((a+b)%c)
print(((a%c) + (b%c)) % c)
print((a*b)%c)
print(((a%c) *(b%c))%c)