import sys 
n = int(sys.stdin.readline())
# 0 <= N <= 500 
# O(N^3)

# 처음 0이 아닌 숫자가 나올 때까지의 0의 개수를 구하는 프로그램

# 팩토리얼의 값
res = 1

def facto(a) :
    global res 

    if a == 0 or a == 1 :
        res *= 1 
        return 

    else :
        res *= a 
        facto(a-1)

# implement function
facto(n)

cnt = 0

for elem in str(res)[::-1] : 
    if elem == '0' :
        cnt += 1
    else :
        break 

print(cnt)