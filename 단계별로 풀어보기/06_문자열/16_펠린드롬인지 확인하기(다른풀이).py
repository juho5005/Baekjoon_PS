import sys 
string = sys.stdin.readline().rstrip()

if string[::-1] == string :
    print(1)
else :
    print(0)