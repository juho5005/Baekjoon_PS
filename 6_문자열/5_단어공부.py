# 이 단어에서 가장 많이 사용된 알파벳을 구하기
# 대소문자 구분 X

import sys 
s = sys.stdin.readline().rstrip() # s <= 1,000,000

alps = []

for elem in s : 
    if ord(elem) >= 97 :
        elem = chr(ord(elem) - 32)
        alps.append(elem)
    else :
        alps.append(elem)

# 알파벳 dictionary 생성 
alphabet_dict = {}
for i in range(65, 91) :
    alphabet_dict[chr(i)] = 0

# 주어진 단어의 알파벳개수를 세어준다
for elem in alps :
    alphabet_dict[elem] += 1

max_value = float('-inf') # 음의 최댓값 

cnt = 0 
want_alp = ''

for val in alphabet_dict.items() :
    alpha, number = val # unpacking

    if number > max_value : 
        max_value = number 
        want_alp = alpha
        cnt = 0

    elif number == max_value : 
        want_alp = alpha
        cnt += 1

if cnt != 0 :
    print('?')

else :
    print(want_alp)
