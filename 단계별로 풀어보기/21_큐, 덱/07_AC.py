# AC > 정수 배열에 연산을 하기 위해 만든 언어 
# 두 가지 함수 R(뒤집기), D(버리기)

# 배열이 비어있을 때 D(버리기)를 사용하면 에러 발생

# 함수는 조합해서 사용 가능 ex) RDD

# 배열의 초기값과 수행할 함수가 주어질 때 최종 결과를 구하시오.

from collections import deque 
import sys 

t = int(sys.stdin.readline()) # 1 <= t <= 100

for _ in range(t) :
    func = sys.stdin.readline().rstrip()
    error = False 
    # 1 <= len(func) <= 100,000 
    # O(1), O(logN), O(N), O(NlogN) : consideration of time complexity 

    n = int(sys.stdin.readline()) # the number of arr

    arr = sys.stdin.readline().rstrip() # show the arr 
    dq = deque() # declaration of deque 

    # split the arr 
    for elem in arr[1:-1].split(',') :
        dq.append(elem)

    R_cnt = 0 # the number of rotate 

    # 길이가 0인 부분에 대해서는 예외사항으로 빈 큐로 초기화
    if n == 0 :
        dq = deque()

    for f in func : 
        if f == 'R' :
            R_cnt += 1

        elif f == 'D' :
            if len(dq) == 0 :
                error = True 
                break 

            if R_cnt % 2 == 0 :
                dq.popleft()
            else :
                dq.pop()
    
    if error :
        print("error")
    else :

        if R_cnt % 2 == 1 :
            dq.reverse()

        print('[', end='')

        for idx,elem in enumerate(dq, start = 1) : 
            if idx == len(dq) :
                print(elem, end='')
            else :
                print(elem, end =',')

        print(']')