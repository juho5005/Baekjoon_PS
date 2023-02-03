# 암호는 서로 다른 L개의 알파벳 소문자로 구성
# 최소 한개의 모음(a, e, i, o, u)
# 최소 두개의 자음(except 모음)

# 알파벳이 증가하는 순서로 배열

# ex) abc (암호 o), bac (암호 x)

# 암호로 사용했을 법한 문자의 종류는 C가지 존재
# C개의 문자들이 모두 주어졌을 때 
# 가능성 있는 암호들을 모두 구하시오

import sys 
l, c = tuple(map(int, sys.stdin.readline().split()))

alphas = list(sys.stdin.readline().rstrip().split())
alphas.sort() # order by asc

ans = []

visited = {}

for alpha in alphas :
    visited[alpha] = 0

vowel = ['a', 'e', 'i', 'o', 'u']

def ans_print() :
    check_vowel = []
    for elem in ans :
        check_vowel.append(elem)
    
    vowel_printing = False
    
    l = len(ans)

    for v in vowel :
        if v in check_vowel :
            vowel_printing = True 
            l -= ans.count(v)

    if vowel_printing and l >= 2 : 
        print(''.join(check_vowel))


# curr_num번째 자리의 숫자를 고르는 choose함수
def choose(curr_num) :
    if curr_num == l+1 :
        ans_print()
        return 
    
    for alpha in alphas : 
        if visited[alpha] == 0 :
            if curr_num != 1 and ord(ans[-1]) > ord(alpha) :
                continue
            visited[alpha] = 1 
            ans.append(alpha)
            choose(curr_num+1)
            ans.pop()
            visited[alpha] = 0
    
choose(1)
