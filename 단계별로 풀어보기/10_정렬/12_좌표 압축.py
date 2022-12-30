# 좌표 x1~xN (N개)
# Xi를 좌표 압축한 X'i값은 Xi>Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1~XN에 좌표 압축을 적용한 결과 X'1~X'N을 출력해보시오.

import sys 
n = int(sys.stdin.readline())
# 1 <= N <= 1,000,000

Xs = list(map(int, sys.stdin.readline().split()))
sorted_Xs = list(set(sorted(Xs)))
sorted_Xs.sort()

dic = {}
for (idx, num) in enumerate(sorted_Xs) :
    dic[num] = idx

for x in Xs :
    print(dic[x], end = ' ')