# N개의 도시
# 제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동
# 인접한 도시 사이의 도로들의 길이는 다를 수 있다.

# 1km마다 1리터의 기름 사용 

# 원 : 그 도시의 주유소 리터당 가격의 단위

import sys 
n = int(sys.stdin.readline()) # 도수의 개수 : N

# 인접한 두 도시를 연결하는 도로의 길이가 N-1개 주어짐
roads = list(map(int, sys.stdin.readline().split()))

# 각 주유소의 기름 가격
oil = list(map(int, sys.stdin.readline().split()))

# 첫 주유소와 첫 거리의 곱은 "무조건" 반영된다는 사실을 이용 
result = oil[0] * roads[0] 

# 최소 기름가격 설정
min_oil = oil[0]

l = len(oil)

for i in range(1, l-1) : 
    if oil[i] < min_oil :
        result += (oil[i] * roads[i])
        min_oil = oil[i]
    else :
        result += (min_oil * roads[i])

print(result)