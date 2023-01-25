# 문자열에 포함되어 있는 
# 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램 작성

import sys 

while 1:
    s = sys.stdin.readline() 

    if not s :
        sys.exit()

    small = 0
    big = 0
    num = 0
    blank = 0

    for elem in s :
        if ord(elem) >= ord('a') and ord(elem) <= ord('z') :
            small += 1 
        elif ord(elem) >= ord('A') and ord(elem) <= ord('Z') :
            big += 1
        elif elem.isdigit() :
            num += 1
        elif elem == ' ' :
            blank += 1

    print(small, big, num, blank)