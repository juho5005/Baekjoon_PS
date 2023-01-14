# 양수, +, -, ( ) 를 가지고 식을 만든다.
# 그리고 나서 괄호를 모두 제거

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드려고 한다.

# 1)가장 처음과 마지막 문자는 숫자
# 2)연속해서 두 개 이상의 연산자가 나타나지 않고
# 3)5자리보다 많이 연속되는 숫자는 없다.

# 30 - (50 + 80) : -가 있고 그다음 연산자가 +이면 괄호로 묶으면 값이 작게 나와준다.

import sys 
s = sys.stdin.readline().rstrip().split('-')

# 식의 최소 결과 값
min_res = 0

# range of list
l = len(s)

for i in range(l) :
    # 첫 번째 일 경우는 더해주는 경우
    if i == 0 :
        if '+' in s[i] : # '+'가 있는 경우
            string_s = ''.join(s[i])

            for elem in string_s.split('+') :
                min_res += int(elem)
        
        else :
            min_res += int(s[i])

    else :
        if '+' in s[i] :
            string_s = ''.join(s[i])

            for elem in string_s.split('+') :
                min_res -= int(elem)

        else :
            min_res -= int(s[i])

print(min_res)
