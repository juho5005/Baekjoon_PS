import sys 

while 1:
    try :
        n = sys.stdin.readline().rstrip()
        if n == '' :
            break 
        print(n)

    except EOFError:
        break 
