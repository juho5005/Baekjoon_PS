import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

a_matrix = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

b_matrix = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# print
for i in range(n) :
    for j in range(m) :
        print(a_matrix[i][j] + b_matrix[i][j], end = ' ')
    print()