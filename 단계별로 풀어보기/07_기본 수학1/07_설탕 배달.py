# 설탕을 N킬로그램 배달 해야함.
# 봉지 -> 3, 5 kg 존재

import sys 
n = int(sys.stdin.readline()) # 3 <= N <= 5000

# 배달하는 봉지의 최소 개수
# 정확하게 N킬로그램을 만들 수 없다면 -1 출력

sack = 0
while n>= 0 :
    if n % 5 == 0 :
        sack += n // 5
        print(sack)
        sys.exit()
    
    sack += 1
    n -= 3

else :
    print(-1)