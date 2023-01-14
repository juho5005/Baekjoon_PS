# 세 변의 길이로 삼각형이 직각인지 아닌지 구분

import sys 
import math

while 1 : 
    x, y, z = list(map(int, sys.stdin.readline().split()))

    lst = [x, y, z]    

    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0 :
        sys.exit() # terminate 

    lst.sort()

    if int(math.pow(lst[0],2)) + int(math.pow(lst[1], 2)) == int(math.pow(lst[2], 2)) :
        print('right')
    else :
        print('wrong')
    