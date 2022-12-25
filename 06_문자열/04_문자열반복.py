import sys 
t=  int(sys.stdin.readline()) # 1 <= T <= 1000
# O(N^2), O(N^2*logN)

for i in range(t) :
    r, s = list(sys.stdin.readline().rstrip().split())
    
    r = int(r) # 정수 변환 
    
    for elem in s :
        print(elem*r, end='')
    print()
