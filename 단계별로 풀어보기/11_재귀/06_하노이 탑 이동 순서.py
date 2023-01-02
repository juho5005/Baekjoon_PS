import sys 

# 한 번에 한 개의 원판만을 다른 탑으로 옮김
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 함

n = int(sys.stdin.readline()) # 장대에 쌓인 원판의 개수 
# 1 <= N <= 20

# 이동 횟수 
k = 0

# 움직임 기록
moves = []

def hanoi(n, first, mid, last) :
    global k
    k += 1

    if n == 1 :
        moves.append([first, last])
    else :
        hanoi(n-1, first, last, mid)
        moves.append([first, last])
        hanoi(n-1, mid, first, last)

# 함수 실행
hanoi(n, '1', '2', '3')

print(k)
for elem in moves : 
    print(*elem)