# 3개를 이용해서 연도를 나타낸다 (지구, 태양, 달)
# 지구(E) : 1<= E <= 15
# 태양(S) : 1<= S <= 28
#   달(M) : 1<= M <= 19

# 1년은 준규의 나라에서는 1 1 1, 즉) 세 수는 모두 1씩 증가
# 어떤 수가 범위를 넘어가는 경우에는 1이 된다.

import sys 
e, s, m = tuple(map(int, sys.stdin.readline().split()))

finish = (e, s, m)

e1, s1, m1 = 1, 1, 1

year = 0 
while 1 :
    year += 1

    if (e1, s1, m1) == finish :
        print(year)
        break 
    
    if (e1+1) <= 15 :
        e1 += 1
    else :
        e1 = 1
    
    if (s1+1) <= 28 :
        s1 += 1
    else :
        s1 = 1
    
    if (m1+1) <= 19 :
        m1 += 1
    else :
        m1 = 1


    