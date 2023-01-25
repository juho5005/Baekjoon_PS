# 네 수 
import sys 

a, b, c, d = tuple(map(int, sys.stdin.readline().split()))

ab = int(str(a) + str(b))
cd = int(str(c) + str(d))

print(ab+cd)