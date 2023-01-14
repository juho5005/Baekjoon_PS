import sys 
t = int(sys.stdin.readline()) # 1 <= t <= 100
# O(N^4) 

for _ in range(t) :
    n = int(sys.stdin.readline()) # 의상의 수 (1<= n <=30)
    
    bundle = dict()

    for _ in range(n) :
        name, kind = sys.stdin.readline().rstrip().split()

        if kind not in bundle :
            bundle[kind] = 1 
        else :
            bundle[kind] += 1
    
    result = 1
    for elem in bundle.values() :
        result *= (elem+1)
    
    print(result-1)