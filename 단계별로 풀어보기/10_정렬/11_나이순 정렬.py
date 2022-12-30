# 나이, 이름이 가입한 순서대로 주어짐

# 1) 나이가 증가하는 순
# 2) 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서

import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 10,000
# O(1), O(logN), O(N), O(NlogN)

age_name_lst = []
for _ in range(n) :
    age, name = tuple(sys.stdin.readline().rstrip().split())
    age = int(age)
    
    age_name_lst.append([age, name])

age_name_lst.sort(key=lambda data:data[0])

for elem in age_name_lst :
    print(*elem)