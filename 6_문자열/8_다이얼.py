# 숫자 1을 거는데 2초 소요
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 소요
import sys 

maching = [('ABC', 3), ('DEF', 4), ('GHI', 5),
('JKL', 6), ('MNO', 7), ('PQRS', 8), ('TUV', 9),
('WXYZ', 10)]

s = sys.stdin.readline().rstrip() # 2 <= s <= 15

cnt = 0
for elem in s : 
    for mach in maching :
        if elem in mach[0] :
            cnt += mach[1] 
            break 
print(cnt)