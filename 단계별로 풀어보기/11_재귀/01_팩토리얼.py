import sys 
n = int(sys.stdin.readline()) # 0보다 크거나 같은 정수 N, N!을 출력하는 프로그램을 작성

cnt = 1

def facto(n) :
    global cnt

    if n == 0 or n == 1 :
        return cnt 
    cnt *= n
    return facto(n-1)

# 함수 실행
print(facto(n))