# 단어 뒤집기 
# 문장이 주어질 때, 단어를 모두 뒤집어서 출력하는 프로그램 작성

import sys 
t = int(sys.stdin.readline())

for _ in range(t) :
    sentence = sys.stdin.readline().rstrip().split()
    
    for elem in sentence : 
        print(elem[::-1], end = ' ')