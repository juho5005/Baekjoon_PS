# MN개의 단위 정사각형으로 나뉘어진 M*N 크기의 보드
# 어떤 것의 색깔 B, 나머지는 W
# 체스판을 색칠하는 경우는 오로지 2가지 
# B와 W는 번갈아서 칠해져야 한다.
# 즉, 변을 공유하는 두개의 사각형은 다른 색으로 칠해져야 함
# 1) 맨 왼쪽 위 칸이 흰색인 경우 2) 맨 왼쪽 위 칸이 검은색인 경우

# 8x8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형으로 다시 칠해야겠다고 생각
# 8x8 크기는 아무데서나 골라도 된다.
# 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성

import sys 
n, m = tuple(map(int, sys.stdin.readline().split())) # 8 <= N, M <= 50

# board_checking
def print_board() :
    for i in range(n) :
        for j in range(m) :
            print(board[i][j], end = ' ')
        print()

# 판 형태 생성
board = [
    [''] * m
    for _ in range(n)
]

# 판 입력받기
for i in range(n) :
    width = sys.stdin.readline().rstrip()
    for j in range(len(width)) :
        board[i][j] = width[j]


min_paint = sys.maxsize

# 8x8로 판을 자르는 모든 경우의 수 생각
for i in range(n-8+1) : # 8만큼 만들 수 있는 세로
    for j in range(m-8+1) : # 8만큼 만들 수 있는 가로
        
        # 다시 칠해야 하는 변의 개수
        cnt_W = 0
        cnt_B = 0 

        for p in range(i, i+8) :
            for q in range(j, j+8) :


                if p % 2 == 0 : # p / 0 2 4 6 
                    if q % 2 == 0 : # q / 0 2 4 6
                        if board[p][q] != 'W' : # 처음이 W
                            cnt_W += 1
                        elif board[p][q] != 'B' : # 처음이 B
                            cnt_B += 1
                    else : # q / 1 3 5 7
                        if board[p][q] != 'B' : # 처음이 W
                            cnt_W += 1
                        elif board[p][q] != 'W' : # 처음이 B
                            cnt_B += 1
                
                else : # p / 1 3 5 7
                    if q % 2 == 0 : # q / 0 2 4 6
                        if board[p][q] != 'B' : # 처음이 W 
                            cnt_W += 1
                        elif board[p][q] != 'W' : # 처음이 B
                            cnt_B += 1
                    else : # q / 1 3 5 7
                        if board[p][q] != 'W' : # 처음이 W
                            cnt_W += 1 
                        elif board[p][q] != 'B' : # 처음이 B
                            cnt_B += 1 

        min_paint = min(min_paint, cnt_W, cnt_B)

print(min_paint)
