import sys 

while 1 : 
    n1, n2 = tuple(map(int, sys.stdin.readline().split()))

    if (n1, n2) == (0, 0) :
        break 
    
    if n2 % n1 == 0 :
        print('factor')
    elif n1 % n2 == 0 :
        print('multiple')
    else :
        print('neither')