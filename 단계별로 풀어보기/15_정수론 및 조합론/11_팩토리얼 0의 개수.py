import sys 
n = int(sys.stdin.readline()) # 0 <= n <= 500
# O(N^3)

# 처음 0이 아닌 숫자가 나올 때 까지 0의 개수를 구하는 프로그램을 작성 

def facto(n) :
    res = 1
    while n >= 1 : 
        res *= n
        n -= 1 
    return str(res)

cnt = 0
for elem in facto(n)[::-1] :
    if elem == '0' :
        cnt += 1 
    else :
        break 
print(cnt)