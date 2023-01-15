# 동생 N명과 숨바꼭질 
# 현재 점 S에 위치
# 동생은 A1, A2, A3 ... AN

# X일 때 1초 후 X+D 또는 X-D 
# 수빈이의 위치가 동생이 있는 위치와 같으면 동생을 찾았다고 간주한다.
# 모든 동생을 찾기위해 D의 값을 정하려고 할 때 
# 가능한 D의 최댓값은 ?

import sys 
n, s = tuple(map(int, sys.stdin.readline().split()))
# 1 <= N <= 10^5 => O(1), O(logN), O(NlogN), O(N)
# 1 <= S <= 10^9 

pos = list(map(int, sys.stdin.readline().split())) # 동생의 위치는 수빈이의 위치와 같지 않다.
# 1 <= pos <= 10^9

if len(pos) == 1 : # 동생이 1명인 경우
    print(abs(s-pos[0]))
    sys.exit()

def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a 

pos_diff = []

for elem in pos : 
    pos_diff.append(abs(elem-s))


max_gcd = pos_diff[0]

for elem in pos_diff : 
    max_gcd = gcd(max_gcd, elem)

print(max_gcd)