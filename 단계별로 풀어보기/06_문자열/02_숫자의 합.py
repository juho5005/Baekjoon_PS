import sys 

# N개의 숫자가 공백없이 쓰여있음
# 이 숫자들을 모두 합해서 출력하시오

n = int(sys.stdin.readline()) # 1 <= N <= 100
nums = list(sys.stdin.readline().rstrip())

cnt = 0
for elem in nums :
    cnt += int(elem)

print(cnt)