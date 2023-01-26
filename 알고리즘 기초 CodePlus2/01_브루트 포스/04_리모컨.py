# 0~9의 숫자
# '+', '-'버튼이 존재
# 0에서 -를 누른 경우에는 채널 변경 x

# 이동하려고 하는 채널이 N
# 채널의 범위는 무한대이다.
# 어떤 버튼이 고장났는지 주어질 때
# 채널 N으로 이동하기 위해서 최소 몇 번 버튼을 눌러야 하는지 구하시오

# 현재채널은 100번

import sys 
# 이동하고자 하는 채널
n = int(sys.stdin.readline()) # 0 <= N <= 500,000

# 고장난 숫자 버튼의 개수
m = int(sys.stdin.readline()) # 0 <= M <= 10

# 숫자 버튼들의 집합
buttons = [
    i
    for i in range(0, 10)
]

# 고장난 버튼이 있을 때
if m != 0 :
    # 고장난 버튼
    broken = list(map(int, sys.stdin.readline().split()))

    # 고장난 숫자 버튼들 제거
    for b in broken  :
        buttons.remove(b)


min_click = float('inf')

# 추가 : 찾고자 하는 채널이 100번 일때(처음 채널의 위치)는 0 출력 후 종료
if n == 100 : 
    print(0)
    sys.exit()

# 경우 1)
# 리모컨의 번호를 이용하지 않고 '+', '-' 버튼으로만 채널 N으로 이동할 때
minus_click = 0
plus_click = 0
start_channel = 100
if n < start_channel : 
    while n != start_channel :
        minus_click += 1
        start_channel -= 1
    min_click = min(min_click, minus_click)

elif n > start_channel : 
    while n != start_channel : 
        plus_click += 1
        start_channel += 1 
    min_click = min(min_click, plus_click)

# 경우2) 리모컨에 고장나지 않은 숫자 버튼으로 근접한 채널로 이동 후
# '+', '-'버튼을 사용하여 N번으로 이동하는 경우
# 물론, 숫자버튼만으로 원하는 채널 N에 도달할 수도 있다.

# 모든 채널을 [일단] 고려
for i in range(1000001) :
    click_cnt = abs(i-n) + int(len(str(i))) # 숫자버튼 누르는 것도 잊으면 안된다.

    if click_cnt < min_click : 
        is_true = True 
        
        for elem in str(i) :
            if int(elem) not in buttons :
                is_true = False 
                break 
        
        if is_true :
            min_click = click_cnt

print(min_click)
