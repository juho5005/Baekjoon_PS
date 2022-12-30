import sys 
a, b = tuple(sys.stdin.readline().rstrip().split())

a = a[::-1]
int(a)
b = b[::-1]
int(b)

if a > b :
    print(a)
else :
    print(b)