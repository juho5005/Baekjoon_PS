import sys 
n = int(sys.stdin.readline())

k = (2*n) - 1
l = k // 2

star = []

for i in range(1, k+1, 2) :
    print(' ' * l + '*' * i)
    l -= 1 

l = 1
for j in range(k-2, -1, -2) :
    print(' ' * l + "*" * j)
    l += 1