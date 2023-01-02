import sys 
n = int(sys.stdin.readline()) # N은 3의 거듭제곱

# 재귀함수 생성
def star_recursion(star) :
    new_star = []

    for i in range(0, 3 * len(star)) :
        if i//len(star) != 1 : 
            new_star.append(3 * star[i % len(star)])
        else :
            new_star.append(star[i%len(star)] + " " * len(star) + star[i%len(star)])
    return new_star

star = ["***", "* *", "***"]

# 재귀 횟수
recursion_cnt = 0

while n != 3 :
    recursion_cnt += 1
    n //= 3

for _ in range(recursion_cnt) :
    star = star_recursion(star)

for elem in star : 
    print(elem)