# 종말의 숫자 : 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수 
# 제일 작은 종말의 숫자 : 666, 1666, 2666, 3666 ~
# 666 1666 2666 3666 4666 5666 6660 ~ 6669(10개)

# N <= 10,000
# N번째 영화의 제목에 들어갈 수는 ?

end_num = '666'

import sys 
n = int(sys.stdin.readline())

start = 666
seq = 0 
while 1 : 
    if end_num in str(start) :
        seq += 1
        
    if n == seq : 
        print(start)
        sys.exit()
        
    start += 1 
