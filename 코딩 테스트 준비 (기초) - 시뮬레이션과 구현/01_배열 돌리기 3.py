import sys 

# 1번 연산
def one() :
    temp = [
        [0] * m
        for _ in range(n)
    ]
    
    for i in range(n) :
        temp[i] = board[n-i-1]
    
    return temp 

# 2번 연산
def two() : 
    temp = [
        [0] * m
        for _ in range(n)
    ]
    
    for i in range(n) :
        for j in range(m) :
            temp[i][j] = board[i][m-j-1]
    
    return temp

# 3번 연산
def three() :
    temp = [
        [0] * n
        for _ in range(m)
    ]
    
    for i in range(m) :
        for j in range(n) :
            temp[i][j] = board[n-1-j][i]
    
    return temp

# 4번 연산
def four() :
    temp = [
        [0] * n
        for _ in range(m)
    ]
    
    for i in range(m) :
        for j in range(n) :
            temp[i][j] = board[j][m-i-1]

    return temp

# 5번 연산
def five() :
    temp = [
        [0] * m
        for _ in range(n)
    ]

    # 4 -> 1
    for i in range(n//2) :
        for j in range(m//2) :
            temp[i][j] = board[i + n//2][j]
    
    # 3 -> 4
    for i in range(n//2, n) :
        for j in range(m//2) :
            temp[i][j] = board[i][j + m//2]
    
    # 2 -> 3
    for i in range(n//2, n) :
        for j in range(m//2, m) :
            temp[i][j] = board[i - n//2][j]
    
    # 1 -> 2
    for i in range(n//2) :
        for j in range(m//2, m) :
            temp[i][j] = board[i][j - m//2]
    
    return temp

# 6번 연산
def six() :
    temp = [
        [0] * m
        for _ in range(n)
    ]

    # 2 -> 1
    for i in range(n//2) :
        for j in range(m//2) :
            temp[i][j] = board[i][j + m//2] # 내 맘
    
    # 1 -> 4
    for i in range(n//2, n) :
        for j in range(m//2) :
            temp[i][j] = board[i - n//2][j] 
    
    # 4 -> 3 
    for i in range(n//2, n) :
        for j in range(m//2, m) :
            temp[i][j] = board[i][j - m//2]
    
    # 3 -> 2 
    for i in range(n//2) :
        for j in range(m//2, m) :
            temp[i][j] = board[i + n//2][j] # 내 맘
    
    return temp

n, m, r = tuple(map(int, sys.stdin.readline().split()))
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

seq_lst = list(map(int, sys.stdin.readline().split()))

for seq in seq_lst : 
    if seq == 1 :
        board = one()
    elif seq == 2 :
        board = two()
    elif seq == 3 :
        board = three()
        n, m = m, n
    elif seq == 4 :
        board = four()
        n, m = m, n
    elif seq == 5 :
        board = five()
    else :
        board = six()

for i in board :
    print(*i)