# A진법을 B진법으로 변환시켜주는 프로그램 
# N진법 : 한 자리에서 숫자를 표현할 때 쓸 수 있는 숫자의 가짓수가 N이라는 뜻

import sys 
a, b = tuple(map(int, sys.stdin.readline().split())) # 2<= A,B <= 30 
# 미래세계에서 사용하는 진법 : A
# 현재 정이가 사용하는 진법 : B

# A진법으로 나타낸 숫자의 자리수의 개수 m(1<=<=25)
m = int(sys.stdin.readline())

a_nums = list(map(int, sys.stdin.readline().split()))

power_idx = 0

res = 0
for elem in a_nums[::-1] :
    res += (elem * (a ** power_idx))
    power_idx += 1

# 변환
transfer_lst = list()

while res != 0 :
    transfer_lst.append(str(res%b)) 
    res //= b 

transfer_lst = transfer_lst[::-1]

print(*transfer_lst)