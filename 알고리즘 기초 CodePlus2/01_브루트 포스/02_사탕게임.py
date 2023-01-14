# n x n 크기에 사탕을 채워둔다. (사탕의 색은 모두 같지않을 수 있다.)
# 사탕의 색이 다른 인접한 두 칸을 선택
# 고른 칸에 들어있는 사탕을 서로 교환한다.
# 이제 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고른 다음 그 사탕을 모두 먹는다.

# 사탕이 채워진 상태가 주어졌을 때 상근이가 먹을 수 있는 사탕의 최대 개수를 구하시오

import sys 
n = int(sys.stdin.readline()) # 3 <= N <= 50

# N x N 판 미연에 생성
board = [
    [''] * n
    for _ in range(n)
]

# 사탕의 색 입력 / 빨간색 : C / 파란색 : P / 초록색 : Z / 노란색 : Y
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
for i in range(n) :
    colors = sys.stdin.readline().rstrip()
    
    for j in range(len(colors)) :
        board[i][j] = colors[j]

# 판 출력
def print_board() :
    for i in range(n) :
        for j in range(n) :
            print(board[i][j], end = ' ')
        print()

max_candy = float('-inf') # 최대로 먹을 수 있는 사탕의 개수

# 인접한 색깔이 다른 사탕을 교환하는 모든 경우를 따져 본 뒤
# 색깔이 같은 가장 긴 사탕을 찾아주면 된다.
# 완전 탐색 유형


def checking_seq_candy() :
    global max_candy

    for i in range(n) :
        cnt = 1 # 길이 비교를 위한 변수
        
        # 열을 따져줌 오른쪽 비교 
        for j in range(1, n) :
            if board[i][j-1] == board[i][j] :
                cnt += 1
            else :
                max_candy = max(max_candy, cnt)
                cnt = 1
        
        # 열이 끝났을 때 계속 이어진 경우 max_candy를 갱신해줘야함
        max_candy = max(max_candy, cnt)

        cnt = 1
        
        # 행을 따져줌 아래쪽 비교
        for j in range(1, n) :
            if board[j-1][i] == board[j][i] :
                cnt += 1
            else :
                max_candy = max(max_candy, cnt)
                cnt = 1
        
        # 행이 끝났을 때 계속 이어진 경우 max_candy를 갱신해줘야함
        max_candy = max(max_candy, cnt)

for i in range(n) :
    for j in range(1, n) :
        
        # 열을 따져줌(오른쪽 비교)
        if board[i][j] != board[i][j-1] :
            board[i][j], board[i][j-1] = board[i][j-1], board[i][j] # 각 사탕을 교환
            
            # 연속으로 이어진 사탕 개수 세어서 최댓값이랑 비교해주기
            checking_seq_candy()

            board[i][j], board[i][j-1] = board[i][j-1], board[i][j] # 교환한 사탕을 원래대로 복귀

        # 행을 따져줌(아래쪽 비교)
        if board[j][i] != board[j-1][i] :
            board[j][i], board[j-1][i] = board[j-1][i], board[j][i] # 각 사탕을 교환


            # 연속으로 이어진 사탕 개수 세어서 최댓값이랑 비교해주기
            checking_seq_candy()

            board[j][i], board[j-1][i] = board[j-1][i], board[j][i] # 교환한 사탕을 원래대로 복귀

print(max_candy)

